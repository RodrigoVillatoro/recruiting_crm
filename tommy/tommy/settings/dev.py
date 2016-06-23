from .base import *

from ..config_secret import cs_DEV_SECRET_KEY


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = cs_DEV_SECRET_KEY

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
