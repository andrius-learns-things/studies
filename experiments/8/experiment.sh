#!/usr/bin/env bash

docker-compose up -d

docker-compose run tester python /code/tester.py -url http://web -times 10

docker-compose run tester python /code/tester.py -url http://web/use-and-release-1kb -times 10


# curl localhost:8059
# docker stats $(docker-compose ps -q)