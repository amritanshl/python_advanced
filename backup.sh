#!/bin/bash

set -euo pipefail

CONFIG_FILE="backup.conf"
declare -A settings
TEMP_DIR=""
TIMESTAMP_FILE=""


log(){
	local level="$1"
	shift
	local msg="$*"
	local timestamp
	timestamp="$(date +"%Y-%m-%d %H:%M:%S")"
	local line="[$timestamp] [$level] $msg"
	echo "$line"
	if [[ -n "${settings[logfile]:-}" ]]; then
		echo "$line" >> "${settings[logfile]}"
	fi
}

send_failure_email() {
    local message="$*"

    local recipient="${settings[alert_email]:-}"
    if [[ -z "$recipient" ]]; then
        # No alert_email configured; nothing to do
        return 0
    fi

    local subject="Backup FAILED on $(hostname)"

    # Try to send the email using the 'mail' command
    echo "$message" | mail -s "$subject" "$recipient" || \
        log ERROR "Failed to send alert email to $recipient"
}


fail() {
	local msg="$*"
    log ERROR "$msg"
    send_failure_email "$msg"

	exit 1
}


load_config() {
	local file="$1"
	if [[ ! -f "$file" ]]; then 
		echo "Config file into found "
		exit 1
	fi
	
	while IFS='=' read -r key value; do
		if  [[ -z "$key" ]]; then
			continue
		fi
		#if [[ "$key" == \#* ]]; then
		#	continue
		#fi
		key="${key//[[:space:]]/}"
        	value="${value#"${value%%[![:space:]]*}"}"
        		

    		settings["$key"]="$value"
	done < "$file"
}

require_setting(){
	local key="$1"
	if [[ -z "${settings[$key]:-}"  ]]; then
		fail "Required settings is missing '$key'"
	fi
}

validate_dir(){
	local path="$1"
	
	if [[ ! -d "$path" ]]; then
		fail "Directory '$path' does not exist"
	fi
	
	if [[ ! -r "$path" ]]; then
		fail "Directory  '$path' is not readable"
	fi

}

setup_temp(){
	TEMP_DIR="$(mktemp -d /tmp/backup_tmp.XXXXXX)"
	log INFO "Created temporary directory: $TEMP_DIR"
}

cleanup(){
	if [[ -n "$TEMP_DIR" && -d "$TEMP_DIR" ]]; then
		log INFO "Cleaning up temporary directories: $TEMP_DIR"
		rm -rf "$TEMP_DIR"
	fi
}
trap cleanup EXIT INT TERM

get_setting(){
	local key="$1"
	printf "${settings[$key]}"

}

backup_full() {
    local src
    src="$(get_setting "source_dir")"

    local dest_dir
    dest_dir="$(get_setting "backup_dir")"

    local date_str
    date_str="$(date +%F)"  # e.g. 2025-12-08

    local dest="$dest_dir/backup-full-$date_str.tar.gz"

    log INFO "Creating FULL backup from '$src' to '$dest'"

    tar -czf "$dest" "$src"

    log INFO "Full backup created at $dest"

    # Update timestamp file to mark the time of this backup
    touch "$TIMESTAMP_FILE"
}


backup_incremental() {
    local src
    src="$(get_setting "source_dir")"

    local dest_dir
    dest_dir="$(get_setting "backup_dir")"

    local date_str
    date_str="$(date +%F)"  # e.g. 2025-12-08

    local dest="$dest_dir/backup-incremental-$date_str.tar.gz"

    # If no previous timestamp exists, do a full backup instead
    if [[ ! -f "$TIMESTAMP_FILE" ]]; then
        log INFO "No previous backup timestamp found; performing FULL backup instead"
        backup_full
        return
    fi

    log INFO "Creating INCREMENTAL backup from '$src' to '$dest' based on '$TIMESTAMP_FILE'"

    # File to store the list of changed files
    local changed_list="$TEMP_DIR/changed_files.txt"

    # Find files in src that are newer than the timestamp file
    find "$src" -type f -newer "$TIMESTAMP_FILE" -print > "$changed_list"

    if [[ ! -s "$changed_list" ]]; then
        log INFO "No files changed since last backup; skipping incremental archive"
        # Still update timestamp so next run is measured from now
        touch "$TIMESTAMP_FILE"
        return
    fi

    # Create a tar.gz containing only the changed files
    tar -czf "$dest" -T "$changed_list"

    log INFO "Incremental backup created at $dest"

    # Update timestamp to now
    touch "$TIMESTAMP_FILE"
}


backup_data() {
    local mode
    mode="$(get_setting "mode")"

    case "$mode" in
        full)
            backup_full
            ;;
        incremental)
            backup_incremental
            ;;
        *)
            fail "Unknown backup mode: '$mode'. Use 'full' or 'incremental'."
            ;;
    esac
}


rotate_backup(){
	local dest_dir
	dest_dir="$(get_setting "backup_dir")"
	
	local days
	days="$(get_setting "retention_days")"
	
	log INFO "Rotating backup older than $days days in '$dest_dir'"
	
	find "$dest_dir" -type f -name "backup-*.tar.gz" -mtime +"$days" -print -exec rm {} \;
	
	log INFO "Old backups removed"
	

}


main(){
	load_config "$CONFIG_FILE"
	require_setting "source_dir"
	require_setting "backup_dir"
	require_setting "retention_days"
	require_setting "logfile"
	
	log INFO "Configuration loaded successfully"
	
	validate_dir "${settings[source_dir]}"
	validate_dir "${settings[backup_dir]}"
	
    TIMESTAMP_FILE="${settings[backup_dir]}/.last_backup_timestamp"
	
	setup_temp
	
	backup_data
	
	rotate_backup
	
	log INFO "Backup process completed successfully"
}

main "$@"














