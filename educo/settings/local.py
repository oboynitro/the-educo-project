from .base import *

DEBUG = True

WSGI_APPLICATION = 'educo.wsgi.local.application'

AUTH_PASSWORD_VALIDATORS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
