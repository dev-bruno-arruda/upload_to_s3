#services.upload_to_s3.py
import os

class UploadToS3:
    @staticmethod
    def upload(s3_service, source_directory, ip_address):
        files_to_upload = os.listdir(source_directory)

        for file_name in files_to_upload:
            file_path = os.path.join(source_directory, file_name)
            if os.path.isfile(file_path):
                new_file_name = f"{ip_address}_{file_name}"
                new_file_path = os.path.join(source_directory, new_file_name)
                os.rename(file_path, new_file_path)
                s3_service.upload_file(new_file_path, new_file_name)
