#!/usr/bin/env bash

docker-compose up -d

curl localhost:8059

docker stats $(docker-compose ps -q)