import os
import json

from .settings import * # flake8: noqa

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = json.loads(os.environ['ALLOWED_HOSTS'])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'facetests',
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_HOST'],
        'PORT': '5432',
    }
}

AWS_STORAGE_BUCKET_NAME = os.environ['BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['BUCKET_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['BUCKET_SECRET_KEY']
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400'
}

AWS_S3_CUSTOM_DOMAIN = '%s.s3-sa-east-1.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/facetests/django.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': True
        },
        'tests_app': {
            'handlers': ['logfile'],
            'level': 'INFO'
        }
    },
}
