# syntax=docker/dockerfile:1
FROM python:3.8.6

WORKDIR /Recipes

ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .