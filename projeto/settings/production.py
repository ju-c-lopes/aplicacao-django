from .settings import *

DEBUG = True

SECRET_KEY = 'alunounivesp'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'settings/db.sqlite3',
    }
}