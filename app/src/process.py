import os
import json
from modules.storage_fetcher import S3StorageFetcher, LocalStorageFetcher

def run_batch_job(storage):
    input_key = 'input.csv'
    output_key = 'output.json'
    local_input_path = '/tmp/input.csv'
    local_output_path = '/tmp/output.json'

    # 1. download
    storage.download(input_key, local_input_path)

    # 2. process
    with open(local_input_path, 'r') as f:
        line_count = sum(1 for _ in f)
    result = {'line_count': line_count}

    # 3. output
    with open(local_output_path, 'w') as f:
        json.dump(result, f)

    storage.upload(local_output_path, output_key)
    print("Job completed.")

if __name__ == '__main__':
    env = os.getenv("ENV", "local")
    if env == "prd":
        fetcher = S3StorageFetcher(bucket_name="eks-test-bucket-20250508")
    else:
        fetcher = LocalStorageFetcher(base_dir="./")

    run_batch_job(fetcher)
