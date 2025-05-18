
# - Import and initialise our environment variables

import environ

env = environ.Env()

environ.Env.read_env()



from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# CSRF_TRUSTED_ORIGINS = []


# Application definition

INSTALLED_APPS = [

     "crispy_forms", # pip install crispy-bootstrap5 之後要key in 的 app之一
    "crispy_bootstrap5", 
    "crispy_bootstrap4",# pip install crispy-bootstrap5 之後要key in 的 app之一
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "journal",
    "storages",

]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5" #意思是bootstrap5版本以下的，像是bootstrap4.bookstrap3..都容許

CRISPY_TEMPLATE_PACK = "bootstap5" #明確地闡述I want to use 的版本


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "edenthought.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "edenthought.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
'''
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
'''

# RDS / PostgreSQL database configuration

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',

        'NAME': env('DB_NAME'), # 設定AWS的RDS時，設定的 initial database name ， 也就是 初始資料庫名稱

        'USER': env('DB_USER'), #設定AWS的RDS時，設定的Master username，也就是主要使用者名稱

        'PASSWORD': env('DB_PASSWORD'), 

        'HOST': env('DB_HOST'), #在RDS建立完database(postgresql)才會知道。 在網頁上顯示的名稱不叫HOST，叫 端點 或 endpoint

        'PORT': '5432',
    }
}





# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


#SMTP Configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = 'True'

EMAIL_HOST_USER = env('EMAIL_HOST_USER') # - GMAIL email address
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD') # - APP password，並不是Gmail的password

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL') # - GMAIL email address


# Amazon S3 configuration


AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME') # - Enter your S3 bucket name HERE

# Django : Storage configuration for S3 --> 把Django的local storage轉到 AWS S3 cloud storage
STORAGES = {

    #Media files（images）management：對應media folder
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },

    # CSS and JS file management:對應static folder

    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}









AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME #創建 unique URLs for 原本在Django裡的 static files，目的在建立安全與具體的路徑

AWS_S3_FILE_OVERWRITE = False




MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'


STATIC_URL = "static/"

STATICFILES_DIRS = [ BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


