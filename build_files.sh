#!/bin/bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py createsuperuser --noinput --username admin --email admin@example.com || true