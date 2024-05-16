#infrastructure.Boto3S3Connector.py
from domain.s3 import S3
from dotenv import load_dotenv

class Boto3S3Connector(S3):
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key):
        super().__init__(bucket_name, aws_access_key_id, aws_secret_access_key)
        load_dotenv()  # Load environment variables from .env file
        import boto3
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    def upload_file(self, file_path, destination):
        print("Fazendo upload", file_path)
        self.s3_client.upload_file(file_path, self.bucket_name, destination)
    
    def list_files(self):
        """Lista os arquivos no bucket."""
        files = []
        bucket = self.s3_resource.Bucket(self.bucket_name)
        for obj in bucket.objects.all():
            files.append(obj.key)
        return files

    def delete_files(self, files):
        """Deleta uma lista de arquivos do bucket."""
        for file in files:
            try:
                self.s3_client.delete_object(Bucket=self.bucket_name, Key=file)
                print(f"Arquivo {file} deletado com sucesso.")
            except Exception as e:
                print(f"Erro ao deletar o arquivo {file}: {e}")