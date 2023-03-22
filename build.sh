#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip
pip install -r requirements.txt

python smakan/manage.py collectstatic --no-input
python smakan/manage.py migrate