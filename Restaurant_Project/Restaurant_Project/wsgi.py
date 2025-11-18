"""
Configuration WSGI pour le projet Resturant_Project.

Elle expose l’appelable WSGI comme une variable au niveau du module nommée application.

Pour plus d’informations sur ce fichier, consultez :
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Resturant_Project.settings')

application = get_wsgi_application()
