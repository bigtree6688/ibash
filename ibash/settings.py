#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Django settings for ibash project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uo%n=b$8964zlau0l!upxj4=__(8c6m#__*2z+egh0=dff*f3w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # 在线上服务器要设置为False

ALLOWED_HOSTS = [] # 在线上服务器要设置该选项


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'frontend',
    'backend',
    'userauth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
# 用户验证模块使用userauth这个app下的UserAuth这个模型
# 位置不能错
# 改变 AUTH_USER_MODEL 对你的数据库结构有很大的影响。
# 它改变了一些会使用到的表格，并且会影响到一些外键和多对多关系的构造。
# 如果你打算设置AUTH_USER_MODEL, 你应该在创建任何迁移或者第一次运行 manage.py migrate 前设置它。
# 在你有表格被创建后更改此设置是不被makemigrations支持的，并且会导致你需要手动修改数据库结构，从旧用户表中导出数据，可能重新应用一些迁移。
AUTH_USER_MODEL = 'userauth.MyUserAuth'

ROOT_URLCONF = 'ibash.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'ibash.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ibash',
        'HOST': '127.0.0.1',
        'PORT': '33306',
        'USER': 'root',
        'PASSWORD': 'www.123',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 用户上传文件的路径
MEDIA_URL = '/image/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')
UPLOAD_PIC_TO = 'article/'# 数据库中是这样的处理的,这里这个变量为了处理用户上传

# 验证码图片的存放路径
VCODE = os.path.join(BASE_DIR, 'static/img/vcode')

# 用户退出登录之后,那些需要用户登录才能打开的页面,需跳转到这个地址请求登录
LOGIN_URL = '/backend/login/'

# email用户名 密码 SMTP服务器 SMTP端口
EMAIL_USER = ''
EMAIL_PWD = ''
EMAIL_SER = ''
EMAIL_PORT = ''

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(filename)s %(module)s %(funcName)s %(lineno)d - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '[%d/%m/%Y %H:%M:%S]',
        },
    },
    'handlers': {
        'request_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/access.log',
            'maxBytes': 1024*1024*10, # 10M
            'backupCount': 7,
            'formatter': 'standard',
        },
        'application_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/application.log',
            'maxBytes': 1024*1024*10, # 10M
            'backupCount': 7,
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['application_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['request_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['request_file'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': False,
        },
    }
}
