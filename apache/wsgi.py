"""
WSGI config for wikiaudia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
import django.core.handlers.wsgi
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wikiaudia.settings")
sys.path.append('/home/ubuntu')
sys.path.append('/home/ubuntu/Wikiaudia_app/Wikiaudia')
sys.path.append('/home/ubuntu/Wikiaudia_app/Wikiaudia/wikiaudia')
from django.core.wsgi import get_wsgi_application
application = django.core.handlers.wsgi.WSGIHandler()
