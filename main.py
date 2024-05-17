import os
import socket
from dotenv import load_dotenv

from services.upload_to_s3 import UploadToS3
from infrastructure.boto3_s3_connector import Boto3S3Connector

load_dotenv()  # Load environment variables from .env file

def upload():
    bucket_name = os.getenv("S3_BUCKET_NAME")
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    source_directory = os.getenv("SOURCE_DIRECTORY")

    s3 = Boto3S3Connector(bucket_name, aws_access_key_id, aws_secret_access_key)
    ip_address = socket.gethostbyname(socket.gethostname())
    UploadToS3.upload(s3, source_directory, ip_address)
    
    # example to delete
    directory = ""
    files, directories = s3.list_files_in_directory(directory)
    s3.delete_files(files)


if __name__ == "__main__":
    upload()
