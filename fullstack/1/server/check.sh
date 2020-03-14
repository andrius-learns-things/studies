#!/bin/bash


black .

if [ $? -ne 0 ]
then
  exit 1
fi


flake8 --config .flake8

if [ $? -ne 0 ]
then
  exit 1
fi


bandit .

if [ $? -ne 0 ]
then
  exit 1
fi