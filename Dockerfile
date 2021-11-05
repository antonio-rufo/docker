FROM python:3.8-slim-buster

ENV SERVICE_PORT="8080"
ENV LOG_LEVEL="INFO"

COPY . /app
WORKDIR /app

RUN apt update \
    && apt upgrade -y \
    && apt install -y git \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt --no-cache-dir

EXPOSE $SERVICE_PORT

ENTRYPOINT [ "python", "server.py" ]
