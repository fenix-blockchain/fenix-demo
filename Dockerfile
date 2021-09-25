FROM python:3-alpine

ENV PYTHONUNBUFFERED=1

RUN pip install fenix-pipeline-sdk
WORKDIR /usr/demo
