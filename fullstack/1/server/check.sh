#!/bin/bash

black .
flake8 --config .flake8  # This is meant to be called from parent dir, therefore path "server/.flake8"