#!/bin/bash

black .
flake8 --config server/.flake8  # This is meant to be called from parent dir, therefore path "server/.flake8"