FROM python:3

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /usr/src/app

RUN pip install -r requirements.txt
