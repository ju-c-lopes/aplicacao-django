#!/usr/bin/env bash
# Exit on error
set -o errexit

# Convert static asset files
python manage.py collectstatic --no-input

# Defining makemigrations
python manage.py makemigrations

# Apply any outstanding database migrations
python manage.py migrate

# Populate the database with initial data
echo ">> Populando dados com Django management command..."
python manage.py init_db --force

# Create Superuser
if [[ "$CREATE_SUPERUSER" == "True" ]]; then
    python manage.py createsuperuser \
        --no-input \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

exec gunicorn --bind 0.0.0.0:8000 projeto.wsgi:application
