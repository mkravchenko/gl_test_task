#!/bin/bash
FROM python:3.8-alpine
RUN mkdir /src
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
RUN ["pytest", "-v", "tests"]