from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('adam', 'admtal@gmail.com'),
)

DOMAIN = 'localhost:8000'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'angel',
        'USER': 'vagrant',
        'PASSWORD': 'localdb',
        'HOST': '',
        'PORT': '',
    }
}