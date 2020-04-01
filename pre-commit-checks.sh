#!/bin/bash

echo "- Checking fullstack/1"

cd fullstack/1
./check.sh

if [ $? -ne 0 ]
then
  echo "FAILED: fullstack/1/check.sh"
  exit 1
fi

cd ..

