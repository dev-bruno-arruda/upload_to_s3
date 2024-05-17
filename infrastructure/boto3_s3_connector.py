import boto3
from dotenv import load_dotenv


class Boto3S3Connector():
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key):
        load_dotenv()  # Load environment variables from .env file
        self.bucket_name = bucket_name
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )
        self.s3_resource = boto3.resource(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    def upload_file(self, file_path, destination):
        print("Uploading", file_path)
        self.s3_client.upload_file(file_path, self.bucket_name, destination)
    
    def list_files(self):
        """List files in the bucket."""
        files = []
        bucket = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
        if 'Contents' in bucket:
            files = [obj['Key'] for obj in bucket['Contents']]
        return files

    def delete_files(self, files):
        """Delete a list of files from the bucket."""
        for file in files:
            try:
                self.s3_client.delete_object(Bucket=self.bucket_name, Key=file)
                print(f"File {file} deleted successfully.")
            except Exception as e:
                print(f"Error deleting file {file}: {e}")

    def delete_files_in_directory(self, directory):
        """Delete all files and subdirectories within the directory in the bucket."""
        objects_to_delete = []
        try:
            # List all objects in the directory
            for obj in self.s3_resource.Bucket(self.bucket_name).objects.filter(Prefix=directory):
                objects_to_delete.append({"Key": obj.key})
            if objects_to_delete:
                # Delete objects
                response = self.s3_client.delete_objects(
                    Bucket=self.bucket_name,
                    Delete={"Objects": objects_to_delete}
                )
                if "Deleted" in response:
                    print(f"All files and subdirectories in '{directory}' were successfully deleted.")
                else:
                    print(f"Error deleting files and subdirectories in '{directory}'.")
            else:
                print(f"No files or subdirectories found in '{directory}' for deletion.")
        except Exception as e:
            print(f"Error deleting files in directory {directory}: {e}")

    def list_files_in_directory(self, directory):
        """List all files and subdirectories within the directory in the bucket."""
        files = []
        directories = []
        try:
            # List all objects in the directory
            for obj in self.s3_resource.Bucket(self.bucket_name).objects.filter(Prefix=directory):
                if obj.key.endswith("/"):
                    directories.append(obj.key)
                else:
                    files.append(obj.key)
            return files, directories
        except Exception as e:
            print(f"Error listing files in directory {directory}: {e}")
            return [], []
