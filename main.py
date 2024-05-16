import os
import socket
from dotenv import load_dotenv

from domain.s3 import S3
from services.upload_to_s3 import UploadToS3


load_dotenv()  # Load environment variables from .env file
def upload():
    bucket_name = os.getenv("S3_BUCKET_NAME")
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    source_directory = os.getenv("SOURCE_DIRECTORY")

    s3_service = S3(bucket_name, aws_access_key_id, aws_secret_access_key)
    ip_address = socket.gethostbyname(socket.gethostname())
    UploadToS3.upload(s3_service, source_directory, ip_address)
    
if __name__ == "__main__":
    upload()