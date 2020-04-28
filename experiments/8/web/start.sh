#!/usr/bin/env bash
service nginx start
uwsgi --ini uwsgi.ini --stats 127.0.0.1:1717 --stats-http