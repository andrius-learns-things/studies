FROM python:3.6-slim

COPY ./ /code/
WORKDIR /code

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

RUN pip install -r requirements.txt

COPY nginx.conf /etc/nginx

CMD ["/bin/sh", "/code/start.sh"]

