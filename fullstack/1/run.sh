#!/bin/bash

./check.sh

if [ $? -ne 0 ]
then
  exit 1
fi

docker-compose up -d