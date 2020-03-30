# Experiment #8 - Memory leak experiments in flask, uwsgi, nginx app

Prerequisites:

1. Docker
2. Docker-compose

To run locally:

`docker build . -t flask_image`

`docker run --name flask_container -p 80:80 flask_image`
