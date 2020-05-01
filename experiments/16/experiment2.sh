#!/usr/bin/env bash

# Set configuration
export EXPERIMENT_NAME="WEB WORKER BOTTLENECK (1 web worker, 10 locust user)"
export EXPERIMENT_WEB_WORKERS="1"
export EXPERIMENT_LOCUST_WEIGHT_INDEX="1"
export EXPERIMENT_LOCUST_WEIGHT_USE_AND_RELEASE="0"
export EXPERIMENT_LOCUST_WEIGHT_USE_AND_LEAK="0"
export EXPERIMENT_LOCUST_USER_COUNT="10"
export EXPERIMENT_WAIT_SECONDS="10"
export EXPERIMENT_EXPECTED_AVG_RESPONSE_TIME="4200"
export EXPERIMENT_EXPECTED_MEMORY_USAGE="25"


# Run:
./experiment_template.sh
