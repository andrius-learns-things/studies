#!/bin/bash

cd server
./check.sh
cd ..

docker-compose up -d