import json
import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = json.loads(os.environ.setdefault('ALLOWED_HOSTS', '[]'))
CSRF_TRUSTED_ORIGINS = json.loads(
    os.environ.setdefault('CSRF_TRUSTED_ORIGINS', '[]')
)
SECURE_PROXY_SSL_HEADER = json.loads(
    os.environ.setdefault('SECURE_PROXY_SSL_HEADER', 'null')
)
USE_X_FORWARDED_HOST = json.loads(
    os.environ.setdefault('USE_X_FORWARDED_HOST', 'false')
)

# Database
DATABASES = json.loads(os.environ.setdefault('DATABASES', json.dumps({
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
})))
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Debugging
DEBUG = json.loads(os.environ.setdefault('DEBUG', 'true'))

# File uploads
DEFAULT_FILE_STORAGE = os.environ.setdefault('DEFAULT_FILE_STORAGE',
    'django.core.files.storage.FileSystemStorage')
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = os.environ.setdefault('MEDIA_URL', 'media/')

# Globalization (i18n/l10n)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# HTTP
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
]
WSGI_APPLICATION = 'www.wsgi.application'

# Models
INSTALLED_APPS = [
    'courses',
    'sync',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django_cleanup.apps.CleanupConfig',
]

# Security
SECRET_KEY = os.environ.setdefault('SECRET_KEY',
    'django-insecure-c^i$dq2#)7ya%++(m$*mirb2+xdvm)jsidbvg4e$!3i)c!m$#f')

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'www.context_processors.canonical',
            ],
        },
    },
]

# URLs
APPEND_SLASH = True
PREPEND_WWW = False
ROOT_URLCONF = 'www.urls'

# Auth
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

# Sites
SITE_ID = json.loads(os.environ.setdefault('SITE_ID', '1'))

# Static Files
STATIC_URL = os.environ.setdefault('STATIC_URL', 'static/')
STATICFILES_DIRS = json.loads(
    os.environ.setdefault('STATICFILES_DIRS', json.dumps(
            [str(BASE_DIR / 'static')]
        )
    )
)
STATICFILES_STORAGE = os.environ.setdefault('STATICFILES_STORAGE',
    'django.contrib.staticfiles.storage.StaticFilesStorage')

# Storages
AWS_S3_ACCESS_KEY_ID = os.environ.setdefault('AWS_S3_ACCESS_KEY_ID', '')
AWS_S3_CUSTOM_DOMAIN = os.environ.setdefault('AWS_S3_CUSTOM_DOMAIN', '')
AWS_S3_ENDPOINT_URL = os.environ.setdefault('AWS_S3_ENDPOINT_URL', '')
AWS_S3_SECRET_ACCESS_KEY = os.environ.setdefault('AWS_S3_SECRET_ACCESS_KEY', '')
AWS_S3_FILE_OVERWRITE = True
