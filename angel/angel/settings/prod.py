from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('adam', 'admtal@gmail.com'),
)

DOMAIN = 'ec2-54-87-180-177.compute-1.amazonaws.com:8000'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'angel',
        'USER': 'ubuntu',
        'PASSWORD': 'localdb',
        'HOST': '',
        'PORT': '',
    }
}