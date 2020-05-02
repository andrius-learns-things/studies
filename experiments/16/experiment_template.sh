#!/usr/bin/env bash

echo "= = = = = = = = = = = = = = = = = = = = = = = = ="
echo "EXPERIMENT: $EXPERIMENT_NAME"

# SETUP

# Set workers for uwsgi
sed -i -e "s#processes = 5#processes = $EXPERIMENT_WEB_WORKERS#g" web/uwsgi.ini

# Set max requests for uwsgi
sed -i -e "s#max-requests = 0#max-requests = $EXPERIMENT_MAX_REQUESTS#g" web/uwsgi.ini

# Configure locust targeted endpoint
sed -i -e "s#task_index: 1, task_use_and_release: 1, task_use_and_leak: 1#task_index: $EXPERIMENT_LOCUST_WEIGHT_INDEX, task_use_and_release: $EXPERIMENT_LOCUST_WEIGHT_USE_AND_RELEASE, task_use_and_leak: $EXPERIMENT_LOCUST_WEIGHT_USE_AND_LEAK#g" locust/locustfile.py

# Configure locust number of users
sed -i -e "s#-c 5#-c $EXPERIMENT_LOCUST_USER_COUNT#g" docker-compose.yml

# RUN

docker-compose up -d --force-recreate

# WAIT
echo "= = = = = = = = = = = = = = = = = = = = = = = = ="
echo "Waiting for $EXPERIMENT_WAIT_SECONDS seconds..."
sleep $EXPERIMENT_WAIT_SECONDS

# CHECK RESULTS

docker-compose logs locust | tail -n 6 > output/locust_results.txt

docker-compose ps -q web | xargs docker stats --no-stream > output/web_server_stats.txt

docker-compose logs web | grep -c "Respawned uWSGI worker" > output/worker_restart_count.txt

echo "= = = = = = = = = = = = = = = = = = = = = = = = ="
echo "Locust results (avg wait time should be approx $EXPERIMENT_EXPECTED_AVG_RESPONSE_TIME):"
cat output/locust_results.txt

echo "= = = = = = = = = = = = = = = = = = = = = = = = ="
echo "Web server stats (mem usage should be approx $EXPERIMENT_EXPECTED_MEMORY_USAGE MB):"
cat output/web_server_stats.txt

echo "= = = = = = = = = = = = = = = = = = = = = = = = ="
echo "Worker restart count (should be approx $EXPERIMENT_EXPECTED_WORKER_RESTART_COUNT):"
cat output/worker_restart_count.txt


# CLEANUP

# Stop
docker-compose down

# Return initial values
sed -i -e "s#processes = $EXPERIMENT_WEB_WORKERS#processes = 5#g" web/uwsgi.ini

# Return initial values
sed -i -e "s#max-requests = $EXPERIMENT_MAX_REQUESTS#max-requests = 0#g" web/uwsgi.ini

# Return initial values
sed -i -e "s#task_index: $EXPERIMENT_LOCUST_WEIGHT_INDEX, task_use_and_release: $EXPERIMENT_LOCUST_WEIGHT_USE_AND_RELEASE, task_use_and_leak: $EXPERIMENT_LOCUST_WEIGHT_USE_AND_LEAK#task_index: 1, task_use_and_release: 1, task_use_and_leak: 1#g" locust/locustfile.py

# Return initial values
sed -i -e "s#-c $EXPERIMENT_LOCUST_USER_COUNT#-c 5#g" docker-compose.yml

# CONCLUSION:

echo "= = = = = = = = = = = = = = = = = = = = = = = = ="
echo "CONCLUSION: $EXPERIMENT_CONCLUSION"
