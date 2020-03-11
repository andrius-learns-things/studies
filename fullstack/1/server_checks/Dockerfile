FROM python:3.8-alpine

# Needed for black (https://github.com/psf/black/issues/1106#issuecomment-547230844)

RUN /sbin/apk add --no-cache --virtual .deps gcc musl-dev \
    && /usr/local/bin/pip install --no-cache-dir black==19.10b0 \
    && /sbin/apk del --no-cache .deps

# Python app dependencies:
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /code