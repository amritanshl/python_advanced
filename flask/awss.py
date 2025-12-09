import boto3

s3 = boto3.client("s3")
# s3.upload_file("flask_app.py","my-training-bucket-123amrit", "my_uploads.py" )
s3.download_file("my-training-bucket-123amrit", "my_uploads.py", "my_downloadfroms3.py")
print("File downloaded successfully")