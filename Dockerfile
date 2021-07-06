FROM python:alpine

ENV PYTHONNUNBUFFERED 1


RUN mkdir /app
WORKDIR /app

COPY . /app/


RUN pip install -r requirements.txt