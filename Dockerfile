FROM python:3.9-slim

WORKDIR /script

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]