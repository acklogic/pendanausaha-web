FROM python:3.8-alpine

LABEL AUTHOR=heritechie@gmail.com

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY  .env /.env

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install -r /requirements.txt \
    && apk del build-deps

RUN mkdir /app
WORKDIR /app
COPY  ./app /app

RUN adduser -D user
USER user