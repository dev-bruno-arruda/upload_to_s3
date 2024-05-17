import os
from datetime import datetime


class UploadToS3:
    @staticmethod
    def upload(s3, source_directory, ip_address):
        files_to_upload = os.listdir(source_directory)

        for file_name in files_to_upload:
            file_path = os.path.join(source_directory, file_name)
            if os.path.isfile(file_path):
                current_date = datetime.now().strftime("%Y%m%d")
                destination = f"{current_date}/{ip_address}_{file_name}"  # Define the complete destination path
                s3.upload_file(file_path, destination)
