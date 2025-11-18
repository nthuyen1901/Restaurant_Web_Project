"""
Configuration ASGI pour le projet Resturant_Project.

Elle expose l’appelable ASGI comme une variable au niveau du module nommée application.

Pour plus d’informations sur ce fichier, consultez :
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Resturant_Project.settings')

application = get_asgi_application()
