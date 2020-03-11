#!/bin/bash

cd server
./check.sh

if [ $? -ne 0 ]
then
  exit 1
fi

cd ..