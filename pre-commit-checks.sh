#!/bin/bash

# Fullstack/1 checks need to pass
cd fullstack/1
./check.sh

if [ $? -ne 0 ]
then
  echo "FAILED: fullstack/1/check.sh"
  exit 1
fi

cd ..

