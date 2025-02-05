#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install poetry -U
poetry install --no-root

# Convert static asset files
python manage.py collectstatic --no-input

# Defining makemigrations
python manage.py makemigrations

# Apply any outstanding database migrations
python manage.py migrate

# Populate the database with initial data
python manage.py init_db

# Create Superuser
if [[ "$CREATE_SUPERUSER" == "True" ]]; then
    python manage.py createsuperuser --no-input
fi
