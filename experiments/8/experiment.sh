#!/usr/bin/env bash

docker-compose up -d

docker-compose run tester python /code/tester.py -url http://web

docker-compose run tester python /code/tester.py -url http://web/use-and-release-1kb


# curl localhost:8059
# docker stats $(docker-compose ps -q)