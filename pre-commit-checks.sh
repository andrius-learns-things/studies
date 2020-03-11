#!/bin/bash

# Fullstack/1 checks need to pass
cd fullstack/1
./check.sh

if [ $? -ne 0 ]
then
  echo "FAILED: fullstack/1/check.sh" >&2
  exit 1
fi

cd ..

