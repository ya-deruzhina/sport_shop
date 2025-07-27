"""
Django settings for internals project.
"""

import datetime
import os
from pathlib import Path
from dotenv import load_dotenv,find_dotenv
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
import pytz

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_FOLDER = os.path.dirname(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# SECRET_KEY = load_dotenv(find_dotenv('SECRET_KEY'))
# ENV = os.getenv('ENV')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # DRF
    'rest_framework',
    'rest_framework_jwt',

    # 3-rd party packages
    'django_extensions',
    'django_filters',
    'corsheaders',

    # Project apps
    'apps.users',
    'apps.shop',
    'internals',

    # Admin
    'smart_selects',

    #Search
    'django_elasticsearch_dsl',
    'apps.search',

    # Django REST framework Elasticsearch integration (this package)
    'django_elasticsearch_dsl_drf',
]

USE_DJANGO_JQUERY = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'internals.middlewares.RequestResponseLoggingMiddleWare',
]

ROOT_URLCONF = 'internals.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'internals.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
    },
}

AUTH_USER_MODEL = 'users.User'
SHELL_PLUS = 'ipython'

SHELL_PLUS_PRE_IMPORTS = [
    ('datetime', ('datetime', 'timedelta')),
]

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_DEFAULT_QUEUE = os.getenv('CELERY_DEFAULT_QUEUE')
CELERY_DEFAULT_EXCHANGE = os.getenv('CELERY_DEFAULT_QUEUE')
CELERY_DEFAULT_ROUTING_KEY = os.getenv('CELERY_DEFAULT_QUEUE')
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# MailCatcher
EMAIL_HOST = '127.0.0.1'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

DEFAULT_FROM_EMAIL  = 'moya_powta@list.ru'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'apps.users.services.auth.authentication_service.JSONWebTokenAuthentication',
    ),
    'EXCEPTION_HANDLER': 'core.utils.exception_handler.exception_handler_wrapper',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 25

}

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

JWT_AUTH = {
    'JWT_SECRET_KEY': JWT_SECRET_KEY,
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=30),
}

# Elasticsearch
# https://django-elasticsearch-dsl.readthedocs.io/en/latest/settings.html

# Name of the Elasticsearch index
ELASTICSEARCH_INDEX_NAMES = {
    'search.documents.documents_for_catalog': 'catalog',
}

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}


TIMEOUT_IN_MINUTES_TIME = int(os.environ.get('TIMEOUT_IN_MINUTES_TIME', 0))


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-client',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMIN_DATE_FORMATS = ('%m/%d/%Y', '%Y-%m-%d')

SERVER_TIMEZONE = pytz.UTC

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

ADMIN_MAX_LOGIN_ATTEMPTS = 3
ADMIN_NEW_LOGIN_TIMEOUT_MINUTES = 15


# the name of the versions will be added to the endpount name as 
# prefix: {HOST}/{version}/{endpoint_name}
# In addition endpoint should be placed
# into urlpatterns to urls_{version}.py file
API_VERSIONS = ('v1', 'v2', )


# Logging configuration
# based on Loguru (https://github.com/Delgan/loguru)
LOGURU_BACKTRACE = True
LOGURU_DIAGNOSE = True
LOG_LEVEL = "INFO"
LOGURU_FORMAT = (
    "[<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>]"
    "[<level>{level}</level>] "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>\n"
)

