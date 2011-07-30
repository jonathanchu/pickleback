import os
import sys

## GLOBAL PATHS
# ---------------------------------------------------------------------------

join = lambda p1,p2: os.path.abspath(os.path.join(p1,p2))

PROJECT = os.path.abspath(os.path.dirname(__file__))
LIBRARIES = join(PROJECT, 'libraries')
APPLICATIONS = join(PROJECT, 'apps')
MEDIA_ROOT = join(PROJECT, 'media')

sys.path.insert(0, LIBRARIES)
sys.path.insert(0, APPLICATIONS)

TEMPLATE_DIRS = (
    join(PROJECT, 'templates'),
)

## DEBUGGING
# ---------------------------------------------------------------------------

DEBUG = True
TEMPLATE_DEBUG = DEBUG

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

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    join(PROJECT, 'static'),
)

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

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
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
    'sentry',
    'sentry.client',

    # pickleback apps
    # 'packages',
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
