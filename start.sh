#!/bin/bash

# Start Gunicorn with 4 workers on localhost port 8000
gunicorn -w 4 -b 0.0.0.0:8000 app:app &

# Start NGINX
nginx -g 'daemon off;'
