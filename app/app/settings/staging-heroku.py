from .base import *
import dj_database_url

import django_heroku

# print(config('DATABASE_URL'))


DEBUG = True

ALLOWED_HOSTS = ['crowdfunapp.herokuapp.com',]

MIDDLEWARE  += ['whitenoise.middleware.WhiteNoiseMiddleware', ]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


django_heroku.settings(locals())
