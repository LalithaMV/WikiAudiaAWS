"""
WSGI config for wikiaudia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import django.core.handlers.wsgi
from wikiaudia.wsgi import 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wikiaudia.settings")
#sys.path.append('/home/ubuntu/Wikiaudia_app/Wikiaudia')
#sys.path.append('/home/ubuntu/Wikiaudia_app/Wikiaudia/wikiaudia')
from django.core.wsgi import get_wsgi_application
application = django.core.handlers.wsgi.WSGIHandler()
