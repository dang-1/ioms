#coding: utf-8
"""
Django settings for ioms project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import json

#login
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$sy@q5kay5c14m7ash3guu#-2j_=g#o5wky5vcn*=^mmb1k7n$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'cmdb.apps.CmdbConfig',
    'hostmanage.apps.HostmanageConfig',
    'sitecollect.apps.SitecollectConfig',
    'blog.apps.BlogConfig',
    'db.apps.DbConfig',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 30
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ioms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ioms.wsgi.application'

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('users:login')

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
db_config = '/Users/tangjianming/config.json'
with open(db_config, 'r') as f:
    db_info = json.load(f)

db_host = db_info['ioms_db_host']
db_port = db_info['ioms_db_port']
db_name = db_info['ioms_db_name']
db_user = db_info['ioms_db_user']
db_password  = db_info['ioms_db_password']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",},
        'HOST': db_host,
        'PORT': db_port,
        'ATOMIC_REQUESTS': True,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCAL_PATHS = [os.path.join(BASE_DIR, 'i18n'), ]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, "data", "static")
STATIC_DIR = os.path.join(BASE_DIR, "static")


STATICFILES_DIRS = (
    os.path.join(BASE_DIR,  'static'),
)

# Custom User Auth model
AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 3
}
DEFAULT_EXPIRED_YEARS = 70
#log
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     # 'filters': {
#     #     'special': {
#     #         '()': 'ioms.logging.SpecialFilter',
#     #         'foo': 'bar',
#     #     },
#     #     'require_debug_true': {
#     #         '()': 'django.utils.log.RequireDebugTrue',
#     #     },
#     # },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'console': {
#             'level': 'INFO',
#             # 'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple',
#         },
#         # 'mail_admins': {
#         #     'level': 'ERROR',
#         #     'class': 'django.utils.log.AdminEmailHandler',
#         #     'filters': ['special']
#         # },
#         'file': {
#             'class': 'logging.FileHandler',
#             'filename': './ioms.log',
#         },
#         # 'ansible_logs': {
#         #         'level': 'DEBUG',
#         #         'class': 'logging.FileHandler',
#         #         'formatter': 'main',
#         #         'filename': os.path.join(PROJECT_DIR, 'logs', 'ansible.log')
#         # },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'level': 'ERROR'
#             # 'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['console', 'file'],
#             'level': 'ERROR',
#             # 'propagate': False,
#         },
#         # 'myproject.custom': {
#         #     'handlers': ['console', 'file'],
#         #     'level': 'INFO',
#         #     # 'filters': ['special']
#         # }
#     }
# }

