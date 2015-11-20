"""
Django settings for django_ecommerce1 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$o7l)_gbjj7tz_vjnrjjh_4ultecb!@sl!84=v)+)!l_lg^seo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DEFAULT_FROM_EMAIL = 'Jianming Chen <loafbaker@hotmail.com>'

# Email Utility
EMAIL_HOST = 'smtp.live.com'  # 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'loafbaker@hotmail.com' # change to your own email address
EMAIL_HOST_PASSWORD = 'yourownpassword' # change to your own password
EMAIL_POT = 25 # default: 587
EMAIL_USE_TLS = True

# Site settings
if DEBUG:
    SITE_URL = 'http://127.0.0.1:8000'
else:
    SITE_URL = 'http://cfestore.com'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'products',
    'carts',
    'orders',
    'accounts',
    'marketing',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'marketing.middleware.DisplayMarketing',
)

ROOT_URLCONF = 'django_ecommerce1.urls'

WSGI_APPLICATION = 'django_ecommerce1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'django_ecommerce1.sqlite'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static_files'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STRIPE_SECRET_KEY = 'sk_test_qDiqoOooh6NBhhcc9AnsT9Qm'

STRIPE_PUBLISHABLE_KEY = 'pk_test_YMB0Ucb4NAP2hurhWfAEHWKT'
