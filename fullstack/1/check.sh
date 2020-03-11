#!/bin/bash

docker-compose run server_checks /bin/sh /code/check.sh

if [ $? -ne 0 ]
then
  exit 1
fi
