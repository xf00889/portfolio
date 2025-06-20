#!/bin/bash
# Start script for Render deployment

echo "Starting gunicorn server..."
gunicorn --bind 0.0.0.0:$PORT portfolio.wsgi:application --log-file - 