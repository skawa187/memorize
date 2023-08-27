# syntax=docker/dockerfile:1

FROM python:alpine3.18

WORKDIR /usr/src/celery/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install pip packages

RUN pip install --upgrade pip --quiet
COPY ./requirements.txt .
RUN pip install -r requirements.txt --quiet

COPY entrypoint.sh .

ENTRYPOINT [ "./entrypoint.sh" ]