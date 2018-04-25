

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r1c-()na3&rqmf35tyk=n=tccb(8tn4bdnhtxd6l%7*3@)c+lx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Custom User Auth model
AUTH_USER_MODEL = 'users.User'


# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'hostmanage.apps.HostmanageConfig',
    'sitecollect.apps.SitecollectConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iomp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iomp.wsgi.application'

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('users:login')

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
db_config = '/Users/tangjianming/config.json'
with open(db_config, 'r') as f:
    db_info = json.load(f)

db_host = db_info['iomp_db_host']
db_port = db_info['iomp_db_port']
db_name = db_info['iomp_db_name']
db_user = db_info['iomp_db_user']
db_password  = db_info['iomp_db_password']
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
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

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
