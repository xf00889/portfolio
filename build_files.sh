#!/bin/bash
# Build script for Render deployment

set -o errexit  # Exit on error
set -o pipefail # Exit on pipe error
set -o nounset  # Exit on variable unset

echo "==================== DEBUGGING INFORMATION ===================="
echo "Python version:"
python --version
echo "Pip version:"
pip --version
echo "Current directory:"
pwd
echo "Directory contents:"
ls -la
echo "=============================================================="

echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Making migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Checking for staticfiles directory..."
if [ -d "staticfiles" ]; then
    echo "Staticfiles directory exists and contains:"
    ls -la staticfiles
else
    echo "WARNING: Staticfiles directory does not exist!"
fi

echo "Build completed successfully!" 