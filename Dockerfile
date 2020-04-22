FROM ubuntu:latest

LABEL maintainer="Sean MacRae <s.mac925@gmail.com>"

RUN apt-get update -y

RUN apt-get install -y python3-pip python3-dev build-essential

COPY requirements.txt /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]