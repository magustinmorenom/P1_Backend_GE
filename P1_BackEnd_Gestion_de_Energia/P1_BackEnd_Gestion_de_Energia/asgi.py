"""
ASGI config for P1_BackEnd_Gestion_de_Energia project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'P1_BackEnd_Gestion_de_Energia.settings')

application = get_asgi_application()
