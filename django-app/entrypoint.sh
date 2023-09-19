#!/bin/sh

if [ "${RUN_MIGRATIONS}" -gt 0 ]
then
    echo 'Running migrations'
    python manage.py migrate
fi
python manage.py collectstatic --noinput

exec "$@"