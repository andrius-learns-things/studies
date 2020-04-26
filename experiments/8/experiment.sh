#!/usr/bin/env bash

docker-compose up -d

docker-compose run tester python /code/tester.py -url web:8059



# curl localhost:8059
# docker stats $(docker-compose ps -q)