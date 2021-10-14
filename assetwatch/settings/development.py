import os
from assetwatch.settings.common import *


DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('NAME'),

        'USER': os.environ.get('USER'),

        'PASSWORD':os.environ.get('PASSWORD'),

        'HOST': 'localhost',

        'PORT': '5432',

    }
}