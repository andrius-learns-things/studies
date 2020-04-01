#!/bin/bash

echo "--- Checking black"

black .

if [ $? -ne 0 ]
then
  exit 1
fi

echo "--- Checking flake8"

flake8 --config .flake8

if [ $? -ne 0 ]
then
  exit 1
fi

echo "--- Checking bandit"

bandit .

if [ $? -ne 0 ]
then
  exit 1
fi