"""
Django settings for FutureResume project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a1o0)i%c5kts^5&k4f7voki#(tv2t)m9z(-d*90(x6tum*_z!w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

####################################################
# If need Email sending function                   #
####################################################
#                                                  #
# EMAIL_HOST = 'smpt.gamil.com'                    #
# EMAIL_HOST_USER = 'youremail@gmail.com'          #
# EMAIL_HOST_PASSWORD = 'your password'            #
# EMAIL_PORT = 587                                 #
# EMAIL_USE_TLS = Ture                             #
#                                                  #
####################################################
# Using gamil, you will need to unlock Captcha to  #
# enable Django to send for you                    #
# https//accounts.google.com/displayunlockcaptcha  #
####################################################



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	# download the django-rest_framework and then grab the fold to the site-package and then add as below, we are success to add in this rest_framework
	'rest_framework',
	# this is about our django app
	'Version_1', #
]



MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'FutureResume.urls'






# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/Users/kentchiu/Django-AE/FutureResume/media'

# MEDIA_ROOT
# models.py 
# class UploadFile(models.Model):
#    file = models.FileField(upload_to='files')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'




TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates') #

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ TEMPLATE_PATH ],
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

WSGI_APPLICATION = 'FutureResume.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'future_resume',
        'USER': 'postgres',
        'PASSWORD': '1Bxpia2a456789',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
###
STATIC_PATH = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/' # You may find this is already defined as such.
STATICFILES_DIRS = (
    STATIC_PATH,
)




# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
##LOGGING = {
##    'version': 1,
##    'disable_existing_loggers': False,
##    'filters': {
##        'require_debug_false': {
##            '()': 'django.utils.log.RequireDebugFalse'
##        }
##    },
##    'handlers': {
##        'mail_admins': {
##            'level': 'ERROR',
##            'filters': ['require_debug_false'],
##            'class': 'django.utils.log.AdminEmailHandler'
##        }
##    },
##    'loggers': {
##        'django.request': {
##            'handlers': ['mail_admins'],
##            'level': 'ERROR',
##            'propagate': True,
##        },
##    }
##}

###