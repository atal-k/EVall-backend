#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Import vans data after migrations
python manage.py import_vans || echo "Skipping import_vans if already imported"