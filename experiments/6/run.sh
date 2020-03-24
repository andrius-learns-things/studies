#!/bin/bash

docker-compose run cli python /code/app.py --name A

docker-compose run cli python /code/app.py --n B

docker-compose run cli python /code/app.py --non-existing-param C