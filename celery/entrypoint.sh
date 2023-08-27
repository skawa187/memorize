#!/bin/sh

celery -A ${CELERY_APP_NAME} worker -l INFO

exec "$@"