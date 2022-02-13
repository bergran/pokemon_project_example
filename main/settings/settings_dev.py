# -*- coding: utf-8 -*-
from main.settings.settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'myproject'),
        'USER': os.environ.get('POSTGRES_USER', 'myproject'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'myproject'),
        'HOST': os.environ.get('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}
