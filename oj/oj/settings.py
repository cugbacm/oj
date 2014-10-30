"""
Django settings for oj project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_PATH='./media'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aa^94ri@un^3y8-1i_vq!)vie3u!mjlilnqf2w^_bs8!$2fn*k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
TIME_ZONE = 'Asia/Shanghai'

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'cugbacm',
    'pagination'
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request"
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.middleware.csrf.CsrfResponseMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'oj.urls'

WSGI_APPLICATION = 'oj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oj',
	   'USER': 'root',
	   'PASSWORD': 'cugbacm',
	   'PORT': '3306',
	   'HOST': '127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'


USE_I18N = True

USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

import djcelery
import sys
djcelery.setup_loader()

CELERY_IMPORTS = (
    'cugbacm.views.problem',
    'cugbacm.views.contest_problem',
)
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
from cugbacm.models import Submit
from datetime import timedelta
from cugbacm.views.problem import Judge, test

CELERYBEAT_SCHEDULE = {
  'add-every-10-seconds': {
    'task': 'cugbacm.views.problem.test',
    'schedule': timedelta(seconds=5),
    'args': (['1000']),
  }
}
CELERY_TIMEZONE = 'Asia/Shanghai'
BROKER_HOST = "127.0.0.1"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/"
if "celeryd" in sys.argv:
    DEBUG = False
