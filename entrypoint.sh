#!/bin/bash
# Apply database migrations
echo "checking migrations"
python manage.py makemigrations
echo "Apply database migrations"
python manage.py migrate
python manage.py collectstatic --noinput

echo "Starting server"

service cron start
echo "starting celery"

celery -A pokemon_battle worker -E -l INFO -f logs/debug_queue.logs -Q default &

# Start server

echo "Starting server"
uwsgi --ini /code/uwsgi.ini

