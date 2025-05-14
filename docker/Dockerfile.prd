FROM python:3.13-slim

WORKDIR /batch

COPY app/src/ .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "process.py"]
