FROM python:3.8-alpine

# Python app dependencies:
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /code/async