#!/usr/bin/env bash
# exit on error
set -o errexit

pwd
which npm

npm install --prefix ./theme/static_src

python -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py tailwind build
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input
fi