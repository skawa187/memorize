#!/bin/sh

python manage.py migrate
python manage.py collectstatic

exec "$@"