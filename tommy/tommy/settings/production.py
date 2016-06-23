from .base import *

from ..config_secret import cs_PROD_DATABASE, cs_PROD_SECRET_KEY


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = cs_PROD_SECRET_KEY

DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#https://help.pythonanywhere.com/pages/UsingMySQL/

DATABASES = cs_PROD_DATABASE
