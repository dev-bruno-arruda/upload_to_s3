#interface.s3_interface.py
from abc import ABC, abstractmethod


class S3Interface(ABC):
    @abstractmethod
    def upload_file(self, file_path, destination):
        pass

    @abstractmethod
    def list_files(self):
        pass

    @abstractmethod
    def delete_files(self, files):
        pass