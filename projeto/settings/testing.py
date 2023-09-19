from .settings import *

DEBUG = False

SECRET_KEY = 'alunounivesp'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'PIC01',
        'USER': 'root',
        'PASSWORD': 'alunounivesp',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}