#!/bin/bash

# Ensure Python and pip are available
PYTHON_BIN=$(which python3.11)
PIP_BIN=$(which pip3.11)

# Install dependencies
$PIP_BIN install -r requirements.txt

# Collect static files
$PYTHON_BIN manage.py collectstatic --noinput
