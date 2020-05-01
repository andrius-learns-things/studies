#!/usr/bin/env bash

echo "EXPERIMENT #1: one worker, simple endpoint"

# SETUP

# Set one worker for uwsgi
sed -i -e "s#processes = 5#processes = 1#g" web/uwsgi.ini

# Configure locust to test index endpoint only
sed -i -e "s#task_index: 1, task_use_and_release: 1, task_use_and_leak: 1#task_index: 1, task_use_and_release: 0, task_use_and_leak: 0#g" locust/locustfile.py

# Configure locust to have 1 user
sed -i -e "s#-c 5#-c 1#g" docker-compose.yml

# RUN

docker-compose up -d --force-recreate

sleep 10

docker-compose logs locust | tail -n 6 > output/locust_results.txt

docker-compose ps -q web | xargs docker stats --no-stream > output/web_server_stats.txt

# CHECK RESULTS


echo "Locust results:"
cat output/locust_results.txt

echo "Web server stats:"
cat output/web_server_stats.txt

# CLEANUP

# Stop
docker-compose down

# Return initial values
sed -i -e "s#processes = 1#processes = 5#g" web/uwsgi.ini

# Return initial values
sed -i -e "s#task_index: 1, task_use_and_release: 0, task_use_and_leak: 0#task_index: 1, task_use_and_release: 1, task_use_and_leak: 1#g" locust/locustfile.py

# Return initial values
sed -i -e "s#-c 1#-c 5#g" docker-compose.yml
