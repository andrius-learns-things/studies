#!/usr/bin/env bash

docker-compose up -d

docker-compose restart web

docker-compose ps -q web | xargs  docker stats --no-stream

docker-compose run tester python /code/tester.py -url http://web -times 100

docker-compose ps -q web | xargs  docker stats --no-stream

docker-compose run tester python /code/tester.py -url http://web/use-and-release-1kb -times 100

docker-compose ps -q web | xargs  docker stats --no-stream

docker-compose run tester python /code/tester.py -url http://web/use-and-leak-1kb -times 100

docker-compose ps -q web | xargs  docker stats --no-stream




# curl localhost:8059
# docker stats $(docker-compose ps -q)
# docker ps -q | xargs  docker stats --no-stream
# docker-compose logs web