#!/bin/sh

echo "Run migrations"
python /home/app/web/manage.py migrate
echo "Run collectstatic"
python /home/app/web/manage.py collectstatic

exec "$@"
