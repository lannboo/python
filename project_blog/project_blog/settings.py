# -*- coding: utf-8 -*
"""
Django settings for project_blog project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*v^3_3tv!z)^14tt!wr#k-o!i9pb-7$06k-77ji8(v$27vj=2t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
AUTH_USER_MODEL = 'blog.UserProfile'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'project_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': False,
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

WSGI_APPLICATION = 'project_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogs',
        'USER': 'root',
        'PASSWORD': 'lanboo',
        'HOST': 'localhost',
        'PORT': '3306',
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


MEDIA_URL = '/uploads/'

MEDIA_ROOT =  os.path.join(BASE_DIR, 'uploads')




#自定义用户model

AUTH_USER_MODEL = 'blog.User'



# 需要在setting中重载AUTH_USER_MODEL





# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

import logging
import django.utils.log
import logging.handlers



#
# DEBUG = True # 通过这种方式可以打开 DEBUG 模式
# LOGGING = {
#     'version': 1,
#      'disable_existing_loggers': True,
#      'formatters': {
#          'simple': {
#              'format': '[%(asctime)s] %(levelname)s : %(message)s'
#          },
#          'verbose': {
#              'format': '[%(asctime)s] %(levelname)s %(module)s %(process)d %(thread)d : %(message)s'
#          },
#          'standard':{
#              'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
#          },
#      },
#      'handlers': {
#          'mail_admins':{
#              'level': 'ERROR',
#              'class': 'django.utils.log.AdminEmailHandler',
#              'include_html': True,
#          },
#          'default': {
#             'level':'DEBUG',
#             'class':'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join('logs/','debug_default.log'),
#             'maxBytes': 1024*1024*5,
#             'backupCount': 5,
#             'formatter':'simple',
#          },
#          'request_handler': {
#              'level':'DEBUG',
#              'class':'logging.handlers.RotatingFileHandler',
#              'filename': os.path.join('logs/','debug_request.log'),
#              'maxBytes': 1024*1024*5,
#              'backupCount': 5,
#              'formatter':'standard',
#          },
#          'scprits_handler': {
#             'level':'DEBUG',
#             'class':'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join('logs/','debug_scprits.log'),
#             'maxBytes': 1024*1024*5,
#             'backupCount': 5,
#             'formatter':'standard',
#          },
#          'console': {
#              'level': 'INFO',
#              'class': 'logging.handlers.RotatingFileHandler',
#              'filename':os.path.join('logs/','info_console.log'),
#              'formatter': 'simple',
#          },
#          'file': {
#              'level': 'INFO',
#              'class':'logging.handlers.RotatingFileHandler',
#              'formatter': 'simple',
#              'filename':os.path.join('logs/','info_file.log'),
#              'maxBytes': 1024*1024*5, # 5 MB
#              'backupCount': 5,
#              'mode': 'a',
#          },
#      },
#      'loggers': {
#          'django': {
#              'handlers': ['file', 'console','request_handler','scprits_handler'],
#              'level':'INFO',
#              'propagate': True,
#          },
#      },
# }
