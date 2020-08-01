#!/usr/bin/env bash

# Set configuration
export EXPERIMENT_NAME="ENDPOINT WHICH USES MEMORY - WAIT LONGER (30s)"
export EXPERIMENT_WEB_WORKERS="20"
export EXPERIMENT_MAX_REQUESTS="0"
export EXPERIMENT_LOCUST_WEIGHT_INDEX="0"
export EXPERIMENT_LOCUST_WEIGHT_USE_AND_RELEASE="1"
export EXPERIMENT_LOCUST_WEIGHT_USE_AND_LEAK="0"
export EXPERIMENT_LOCUST_USER_COUNT="20"
export EXPERIMENT_WAIT_SECONDS="30"
export EXPERIMENT_EXPECTED_AVG_RESPONSE_TIME="1000"
export EXPERIMENT_EXPECTED_MEMORY_USAGE="80"
export EXPERIMENT_EXPECTED_WORKER_RESTART_COUNT="0"
export EXPERIMENT_CONCLUSION="Waited longer, but memory usage stayed as with 10s. No memory leak"


# Run:
./experiment_template.sh
