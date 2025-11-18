"""
Paramètres Django pour le projet Restaurant_Project.

Généré par la commande django-admin startproject avec Django 5.0.6.

Pour plus d’informations sur ce fichier, consultez :
https://docs.djangoproject.com/en/5.0/topics/settings/

Pour la liste complète des paramètres et leurs valeurs, consultez :
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Charger les variables d’environnement depuis le fichier .env.
load_dotenv()

# Construire les chemins à l’intérieur du projet comme ceci : BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Paramètres de développement pour un démarrage rapide – non adaptés à la production.
# Consultez : https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


SECRET_KEY = 'django-insecure-t_!n%3ph(-bpkd2+z2!zujx+6r_x%&3%allmra#8#x0v*iogzf'


DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Base_App',
    'django_extensions',
]


SESSION_ENGINE = 'django.contrib.sessions.backends.db'

LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Restaurant_Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Template'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Restaurant_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Mot de passe validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalisation
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = 'static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR / "static")]

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

# Type de champ de clé primaire par défaut
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587  
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'huyenngo1901@gmail.com'  
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD') #
DEFAULT_FROM_EMAIL = 'huyenngo1901@gmail.com'  


GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'  
LOGOUT_REDIRECT_URL = '/login/'  


