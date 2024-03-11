from .settings import *

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com', 'localhost', '*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'projeto/settings/db.sqlite3',
    }
}