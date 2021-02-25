#!/bin/sh

# Apply database migrations
echo "Applying database migrations ..."
python manage.py migrate

# Create superuser
echo "Creating superuser ..."
python manage.py createsuperuser --noinput

# Start server
echo "Starting server ..."
# For prod
# gunicorn --bind 0.0.0.0:8000 my_social_network.wsgi
# For dev
python manage.py runserver 0.0.0.0:8000

