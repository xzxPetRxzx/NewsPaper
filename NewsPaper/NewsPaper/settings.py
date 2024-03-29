"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h#e3+vyd1)ep)nph(cd^q(j_spm^mam4_pl+1e4j*2gh!!aw92'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news',
    'accounts',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

]

LOGIN_URL = '/accounts/login/'
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

CELERY_BROKER_URL = 'redis://default:zxXn9Qm9IH96aIQn7tGmfih3Uf3GXs4t@redis-16421.c258.us-east-1-4.ec2.cloud.redislabs.com:16421'
CELERY_RESULT_BACKEND = 'redis://default:zxXn9Qm9IH96aIQn7tGmfih3Uf3GXs4t@redis-16421.c258.us-east-1-4.ec2.cloud.redislabs.com:1642'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

ADMINS = (
    ('admin', 'garamet1989@yandex.ru'),
)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
LOGIN_REDIRECT_URL = '/news/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_FORMS = {'signup': 'news.forms.CommonSignupForm'}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'garamet1989@yandex.ru'
EMAIL_HOST_PASSWORD = 'Zxcvbnm01'
DEFAULT_FROM_EMAIL = 'garamet1989@yandex.ru'
#EMAIL_USE_SSL = True
EMAIL_USE_TLS = True


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style' : '{',
    'formatters': {
        'simple': {
            'format': '%(asctime)s%(levelname)s%(message)s'
        },
        'warning': {
            'format': '%(pathname)s'
        },
        'error': {
            'format': '%(exc_info)s'
        },
        'genseclog': {
            'format': '%(asctime)s%(levelname)s%(module)s%(message)s'
        },
        'errlog': {
            'format': '%(asctime)s%(levelname)s%(message)s%(pathname)s%(exc_info)s'
        },
        'mailf': {
            'format': '%(asctime)s%(levelname)s%(message)s%(pathname)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'consoleW': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning'
        },
        'consoleE': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'mailf'
        },
        'genlog': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': '/logs/general.log',
            'formatter': 'genseclog'
        },
        'seclog': {
            'class': 'logging.FileHandler',
            'filename': '/logs/security.log',
            'formatter': 'genseclog'
        },
        'errlog': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/logs/errors.log',
            'formatter': 'errlog'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'consoleW', 'consoleE', 'genlog'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errlog', 'mail_admins'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['errlog', 'mail_admins'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['errlog'],
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['errlog'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['seclog'],
            'propagate': True,
        }
    }
}

