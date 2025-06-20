#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements-render.txt

# Collect static files
python manage.py collectstatic --noinput 