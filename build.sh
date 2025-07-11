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
echo ">> Populando dados com Django management command..."
python manage.py init_db --force

# Create Superuser
if [[ "$CREATE_SUPERUSER" == "True" ]]; then
    echo ">> Verificando se superusuário já existe..."
    RESULT=$(python manage.py shell -c "from django.contrib.auth import get_user_model; print(get_user_model().objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists())")
    USER_EXISTS=${RESULT: -5}

    if [[ "$USER_EXISTS" == "False" ]]; then
        echo ">> Criando superusuário padrão..."
        python manage.py createsuperuser \
            --no-input \
            --username "$DJANGO_SUPERUSER_USERNAME" \
            --email "$DJANGO_SUPERUSER_EMAIL"

        echo ">> Definindo senha do superusuário..."
        python manage.py shell -c "
from django.contrib.auth.models import User;
u = User.objects.get(username='$DJANGO_SUPERUSER_USERNAME');
u.set_password('$DJANGO_SUPERUSER_PASSWORD');
u.save()
"
    else
        echo "⚠️ Superusuário já existe. Pulando criação."
    fi
fi
