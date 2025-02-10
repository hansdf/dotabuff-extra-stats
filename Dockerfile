FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3.9 python3.9-dev python3-pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .


