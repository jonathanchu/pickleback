import os
import sys

## GLOBAL PATHS
# ---------------------------------------------------------------------------

ez_path = lambda p1,p2: os.path.abspath(os.path.join(p1,p2))

PROJECT = os.path.abspath(os.path.dirname(__file__))
LIBRARIES = ez_path(PROJECT, 'libraries')
APPLICATIONS = ez_path(PROJECT, 'apps')
MEDIA_ROOT = ez_path(PROJECT, 'media')

sys.path.insert(0, LIBRARIES)
sys.path.insert(0, APPLICATIONS)

TEMPLATE_DIRS = (
    ez_path(PROJECT, 'templates'),
)

## DEBUGGING
# ---------------------------------------------------------------------------

DEBUG = True
TEMPLATE_DEBUG = True

ADMINS = (
    ('Jonathan Chu', 'jc@3atmospheres.com'),
    ('Nick Ficano', 'nf@3atmospheres.com'),
    ('Bjarni Juliusson', 'bj@3atmospheres.com'),
)

MANAGERS = ADMINS

## DATABASE
# ---------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pickleback',
        'USER': 'pickleback',
        'PASSWORD': 'nohZ2xe8ieK9eete',
        'HOST': '',
        'PORT': '',
    }
}

## LOCALE
# ---------------------------------------------------------------------------

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True    # load the internationalization
USE_L10N = True    # format time accounding to current locale

## MEDIA
# ---------------------------------------------------------------------------

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

## STATIC
# ---------------------------------------------------------------------------

STATIC_ROOT = ez_path(PROJECT, 'static')
STATIC_URL = '/static/'

## INTERNALS
# ---------------------------------------------------------------------------

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'pickleback.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # third party apps
    'gunicorn',

    # pickleback apps
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


## AUTHENTICATION
# ---------------------------------------------------------------------------

SECRET_KEY = '+5c(@)zhti_48u+=2o9+xoe2%=&qo_c)c5)!lpl!379m9e=-g0'

## ENVIRONMENTS
# ---------------------------------------------------------------------------

try:
    from local_settings import *
except ImportError:
    pass
