"""
Django settings for gomartnow project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / ''

STATIC_DIR = BASE_DIR / ""
MEDIA_ROOT = BASE_DIR / ""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a-*=177(1128_tqr^&rrl%96&6q-7q25ztvayjep@l=9*uyklk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'False'

ALLOWED_HOSTS = ['.vercel.app','127.0.0.1','localhost:8000','localhost:3000','localhost',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
        'gomartapp',
         'corsheaders',
          'rest_framework',
    'rest_framework.authtoken',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
        #  'whitenoise.middleware.WhiteNoiseMiddleware',

     'django.contrib.sessions.middleware.SessionMiddleware',
    #  'django.middleware.csrf.CsrfViewMiddleware',
     'django.contrib.auth.middleware.AuthenticationMiddleware',
        'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
  
]
# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    # "http://localhost:8000",

    
    "http://127.0.0.1:8000",
]
# CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOW_METHODS = [
#     'DELETE',
#     'GET',
#     'OPTIONS',  # Include OPTIONS if needed
#     'PATCH',
#     'POST',
#     'PUT',
# ]


# CSRF_TRUSTED_ORIGINS = [
#     "http://localhost:3000",
#      "http://localhost:8000",

    
#     "http://127.0.0.1:8000",
# ]

ROOT_URLCONF = 'gomartnow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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
# CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = False
# CSRF_COOKIE_NAME = 'csrftoken'



WSGI_APPLICATION = 'gomartnow.wsgi.application'



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)
# AUTH_USER_MODEL = 'gomartapp.User'

# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',  # Default backend for built-in user model
#     'gomartapp.custom_auth.UserBackend',   # Replace 'gomartapp' with your app's name
# ]

# PASSWORD_HASHERS = [
#     'django.contrib.auth.hashers.PBKDF2PasswordHasher',
#     # Add any other hashers you want to use here
# ]
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = '/static/'

STATICFILES_DIRS = [

os.path.join(BASE_DIR,'gomart/build/static')
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'gomart/build')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'gomart/build')
# os.path.join(BASE_DIR,'gomart/build')

# Define the URL prefix for serving media files.
# MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/api/login/'


# LOGIN_URL = '/api/login/'  # Replace with your actual login URL
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
         'rest_framework.authentication.TokenAuthentication',
    ],
}
# ALLOWED_HOSTS = ["http://localhost:3000", "http://127.0.0.1:8000",]
# CSRF_TRUSTED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:8000",]
# CSRF_ALLOWED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:8000",]
# CORS_ORIGINS_WHITELIST = ["http://localhost:3000", "http://127.0.0.1:8000",]
# settings.py
# WEBPACK_LOADER = {
#     'DEFAULT': {
#         'BUNDLE_DIR_NAME': 'bundles/',
#         'STATS_FILE': os.path.join(BASE_DIR, 'gomart', 'webpack-stats.json'),
#     }
# }
