"""
WSGI config for arthurneyer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import django

from django.core.wsgi import get_wsgi_application

os.getenv('DJANGO_SETTINGS_MODULE', 'arthurneyer.production')
django.setup()

application = get_wsgi_application()
