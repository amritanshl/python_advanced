# #!/bin/bash

# # name="Amrit"

# # show_names(){
# #     name="Local Name"
# #     echo "Inside function: $name"
# # }

# # echo "before function: $name"
# # show_names
# # echo "after function: $name"


# # password="Amritansh###lal"
# # if [ ${#password} -ge 8 ]; then
# #     echo "Password is good. Length of password is ${#password}"
# # else
# #     echo "Password is too short"
# # fi
# #       0           1       2       3       4
# name11=("Chanchal" "Saeed" "Sam" "Aditya" "Sanjana")
# # echo ${name11[@]}
# # echo ${name11[3]}

# name11+=("Lalit" "Aniket")
# # echo ${name11[@]}
# unset name11[2]
# # echo ${name11[@]}
# for a in "${name11[@]}"; do
#      echo "Hello, $a"
# done
# {
#     [
# "name":"Amrit",
# "phone":99999,
# "Address":"New Delhi",
# "Gender":"Male",
# "Marital Status":False
# ],
# [
# "name":"Chanchal",
# "phone":88888,
# "Address":{
#     "present Addreess":"Mumbai",
#     "permanent Address": "Banglore"
# },
# "Gender":"Female",
# "Marital Status":True
# ]
# }
# declare -A aadhar
# aadhar[name]="Amritansh Lal"
# aadhar[number]="45454412"
# aadhar[city]="New Delhi"
# aadhar[phone]=99999999
# aadhar[age]=28

# order=(name number city phone age)
# # echo "${aadhar[city]}"

# echo "{"
# for k in "${order[@]}"; do
#     echo "  \"$k\":  \"${aadhar[$k]}"
# done

# echo "}"


# declare -A settings
# while IFS='=' read -r key value; do
#     settings[$key]=$value
# done < app.conf

helloFromAmrit() 
{
    return "Hello from Amrit"
}
helloFromAmrit




# add() {
#     echo "$(( $1 + $2 ))"
# }


# sub() {
#     echo "$(( $1 - $2 ))"
# }

# mul() {
#     echo "$(( $1 * $2 ))"
# }

# div() {
#     echo "$(( $1 / $2 ))"
# }

# echo "enter first num: "
# read num1
# echo "enter second num: "
# read num2
# echo "choose operation"
# echo "1. Add"
# echo "2. Sub"
# echo "3. Mul"
# echo "4. Div"
# read choice

# case $choice in 
#     1) add "$num1" "$num2" ;;
#     2) sub "$num1" "$num2" ;;
#     3) mul "$num1" "$num2" ;;
#     4) div "$num1" "$num2" ;;
#     *) echo "Invalid Choice" ;;
# esac
    










