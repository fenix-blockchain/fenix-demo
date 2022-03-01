FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

RUN pip install fenix-pipeline-sdk
WORKDIR /usr/demo
