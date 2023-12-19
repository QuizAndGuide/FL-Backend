#!/bin/bash

# Collect static files
python manage.py collectstatic 

# Start server
echo "Starting server"
gunicorn --bind 0.0.0.0:8000 football_quiz.wsgi:application