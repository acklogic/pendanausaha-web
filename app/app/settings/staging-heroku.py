from .base import *

import django_heroku

DEBUG = True

ALLOWED_HOSTS = ['crowdfunapp.herokuapp.com', ]

MIDDLEWARE  += ['whitenoise.middleware.WhiteNoiseMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


django_heroku.settings(locals())
