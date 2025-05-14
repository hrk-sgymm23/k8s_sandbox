import boto3
import os
import shutil
from abc import ABC, abstractmethod

bucket_name = 'eks-test-bucket-20250508'
input_key = 'input/data.csv'
output_key = 'output/result.json'

class StorageFetcher(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def download(self, key, local_path):
        pass

class S3StorageFetcher(StorageFetcher):
    def __init__(self, bucket_name):
        self.client = boto3.client('s3')
        self.bucket_name = bucket_name

    def download(self, key, local_path):
        self.client.download_file(self.bucket_name, key, local_path)

    def upload(self, local_path, key):
        self.client.upload_file(local_path, self.bucket_name, key)


class LocalStorageFetcher(StorageFetcher):
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def download(self, key, local_path):
        src_path = os.path.join(self.base_dir, key)
        shutil.copy(src_path, local_path)

    def upload(self, local_path, key):
        dst_path = os.path.join(self.base_dir, key)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        shutil.copy(local_path, dst_path)