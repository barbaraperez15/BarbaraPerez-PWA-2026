#!/bin/bash

set -e

if [ ! -f manage.py ]; then
    django-admin startproject app .
fi

python manage.py makemigrations
python manage.py migrate --noinput

if [[ -n "${DJANGO_SU_NAME:-}" || -n "${DJANGO_SU_EMAIL:-}" || -n "${DJANGO_SU_PASSWD:-}" ]]; then
    : "${DJANGO_SU_NAME:?DJANGO_SU_NAME must be set to create the superuser}"
    : "${DJANGO_SU_EMAIL:?DJANGO_SU_EMAIL must be set to create the superuser}"
    : "${DJANGO_SU_PASSWD:?DJANGO_SU_PASSWD must be set to create the superuser}"

    python manage.py shell <<'PY'
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ["DJANGO_SU_NAME"]

if User.objects.filter(username=username).exists():
    print("Configured superuser already exists; leaving it unchanged.")
else:
    User.objects.create_superuser(
        username=username,
        email=os.environ["DJANGO_SU_EMAIL"],
        password=os.environ["DJANGO_SU_PASSWD"],
    )
    print("Configured superuser created.")
PY
fi

python manage.py runserver 0.0.0.0:8000