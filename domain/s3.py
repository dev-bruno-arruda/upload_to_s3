# infrastructure/s3_connector.py
import os
import boto3
from datetime import datetime

from interface.s3_interface import S3Interface


class S3(S3Interface):
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key):
        super().__init__()  # Chama o método __init__ da classe pai (S3Interface)
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

    # def upload_file(self, file_path, directory_name):
    #     print("Fazendo upload", file_path)
    #     current_date = datetime.now().strftime("%Y%m%d")
    #     destination = f"{directory_name}/{current_date}/{file_path}"  # Define o caminho completo do destino com o diretório
    #     self.s3_client.upload_file(file_path, self.bucket_name, destination)

    def upload_file(self, file_path, directory_name):
        print("Fazendo upload", file_path)
        current_date = datetime.now().strftime("%Y%m%d")
        destination = f"{current_date}/{os.path.basename(file_path)}"  # Define o caminho completo do destino
        self.s3_client.upload_file(file_path, self.bucket_name, destination)

    def list_files(self):
        """Lista os arquivos no bucket."""
        files = []
        response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
        if 'Contents' in response:
            files = [obj['Key'] for obj in response['Contents']]
        return files

    def delete_files(self, files):
        """Deleta uma lista de arquivos do bucket."""
        for file in files:
            try:
                self.s3_client.delete_object(Bucket=self.bucket_name, Key=file)
                print(f"Arquivo {file} deletado com sucesso.")
            except Exception as e:
                print(f"Erro ao deletar o arquivo {file}: {e}")

    def create_directory(self, directory_name):
        """Cria um diretório no bucket com o formato 'yyyymmdd'."""
        current_date = datetime.now().strftime("%Y%m%d")
        directory_key = f"{directory_name}/{current_date}/"  # Define o caminho do diretório no bucket
        try:
            self.s3_client.put_object(Bucket=self.bucket_name, Key=directory_key)
            print(f"Diretório {directory_key} criado com sucesso.")
        except Exception as e:
            print(f"Erro ao criar o diretório {directory_key}: {e}")
    
    def delete_files_in_directory(self, directory):
        """Deleta todos os arquivos e subdiretórios dentro do diretório no bucket."""
        objects_to_delete = []
        # Listar todos os objetos no diretório
        for obj in self.s3_resource.Bucket(self.bucket_name).objects.filter(Prefix=directory):
            objects_to_delete.append({"Key": obj.key})
        if objects_to_delete:
            # Deletar objetos
            response = self.s3_client.delete_objects(
                Bucket=self.bucket_name,
                Delete={"Objects": objects_to_delete}
            )
            if "Deleted" in response:
                print(f"Todos os arquivos e subdiretórios em '{directory}' foram excluídos com sucesso.")
            else:
                print(f"Erro ao excluir arquivos e subdiretórios em '{directory}'.")
        else:
            print(f"Nenhum arquivo ou subdiretório encontrado em '{directory}' para exclusão.")

    def list_files_in_directory(self, directory):
            """Lista todos os arquivos e subdiretórios dentro do diretório no bucket."""
            files = []
            directories = []
            # Listar todos os objetos no diretório
            for obj in self.s3_resource.Bucket(self.bucket_name).objects.filter(Prefix=directory):
                if obj.key.endswith("/"):
                    directories.append(obj.key)
                else:
                    files.append(obj.key)
            return files, directories