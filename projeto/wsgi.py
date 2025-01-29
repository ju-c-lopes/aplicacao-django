"""
WSGI config for projeto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

from projeto.settings import settings
import logging

logger = logging.getLogger(__name__)


path = os.getcwd()
if path not in sys.path:
    sys.path.insert(0, path)

os.environ["DJANGO_SETTINGS_MODULE"] = "projeto.settings.settings"

# if getattr(settings, "INIT_DB_ON_STARTUP", False):
try:
    # call_command("init_db")
    settings.INIT_DB_ON_STARTUP = False
except Exception as e:
    logger.error(f"Erro ao executar init_db: {e}")
    print(f"Erro ao executar init_db: {e}")

application = get_wsgi_application()
