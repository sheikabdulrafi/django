#!/bin/bash
echo "started build"
# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic
echo "done collecting static files"
echo 'build complete'