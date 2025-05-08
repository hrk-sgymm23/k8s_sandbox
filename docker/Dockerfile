FROM python:3.13-slim

WORKDIR /batch

# 必要なファイルをコピー
COPY app/src/ .

# 必要であれば依存パッケージのインストール（コメントアウト中）
# RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "batch_processing.py"]
