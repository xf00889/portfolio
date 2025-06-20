#!/bin/bash
# Build script for Render deployment

echo "Building the project..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Making migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!" 