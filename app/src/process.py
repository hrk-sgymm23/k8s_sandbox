import boto3

s3 = boto3.client('s3')
bucket_name = 'eks-test-bucket-20250508'
input_key = 'input/data.csv'
output_key = 'output/result.json'

# 1. S3 からファイルをダウンロード
print('##############')
print('bucket_name', bucket_name)
print('input_key', input_key)
print('output_key', output_key)
print('##############')

s3.download_file(bucket_name, input_key, '/tmp/data.csv')

# 2. ここでバッチ処理（例: 行数を数えるだけ）
with open('/tmp/data.csv', 'r') as f:
    line_count = sum(1 for _ in f)

result = {'line_count': line_count}

# 3. 結果をファイルに書き出し
import json
with open('/tmp/result.json', 'w') as f:
    json.dump(result, f)

# 4. S3 にアップロード
s3.upload_file('/tmp/result.json', bucket_name, output_key)

print("Batch job completed and result uploaded to S3.")
