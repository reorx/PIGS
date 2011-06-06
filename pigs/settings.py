# Django settings for my_PIGS project.
import os
ROOT_PATH = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': 'PIGS',                      # Or path to database file if using sqlite3.
        'NAME': os.path.join(ROOT_PATH, '../test/db.sqlite'),
        #'USER': 'root',                      # Not used with sqlite3.
        'USER': '',
        #'PASSWORD': 'mx320lf2',                  # Not used with sqlite3.
        'PASSWORD': '',
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('zh', 'Chinese'),
    ('zh-cn', 'Chinese'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(ROOT_PATH, '../static/media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4x+lg84h@$w^d+e$w197!!vy9w!a(oe2ae!xe+5m$n8*+cwuef'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'pigs.urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, '../templates')
)

INSTALLED_APPS = (
    # authentication essential #
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # admin #
    'django.contrib.admin',
    # filters #
    'django.contrib.markup',
    # utils #
    'utils',
    # modules #
    'knowledge',
    'tag',
    'note',
    # apps #
    #'apps',
)

# account about
LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'
