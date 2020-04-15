#!/bin/bash

docker-compose up -d

dotnet run --project EventSourcing.NetCore/Sample/EventSourcing.Sample.Web