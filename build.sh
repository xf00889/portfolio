#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install --upgrade pip
pip install --timeout=100 -r requirements-deploy.txt

# Collect static files
python manage.py collectstatic --noinput 