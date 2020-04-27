FROM python:3.6.10-slim-stretch

LABEL maintainer="Sean MacRae <s.mac925@gmail.com>"

RUN apt-get update -y \
  && apt-get install -y python3-pip python3-dev build-essential \
  && pip3 install --upgrade pip

COPY requirements.txt /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]