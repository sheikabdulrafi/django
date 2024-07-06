#!/bin/bash

# Ensure Python and pip are available
export PATH="/usr/local/bin:$PATH"

# Install dependencies
pip install -r requirements.txt

# Collect static files
python3.11 manage.py collectstatic --noinput
