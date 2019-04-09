import os
import ast

from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ast.literal_eval(os.getenv('DEBUG', 'True'))

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [

	# Admin Theme Apps
	'admin_interface',
	'colorfield',

	# Django Apps
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.humanize',
	'django.contrib.sites',

	# Third-Party Apps
	'corsheaders',
	'django_filters',
	'rest_framework',
    'ckeditor',

	# Local Apps (Your project's apps)
	#'api.apps.ApiConfig',
    'mailings.apps.MailingsConfig',  #
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'corsheaders.middleware.CorsPostCsrfMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': os.getenv('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
		'NAME': os.getenv('DATABASE_NAME', os.path.join(BASE_DIR, 'db.sqlite3')),
		'USER': os.getenv('DATABASE_USER', ''),
		'PASSWORD': os.getenv('DATABASE_PASSWORD', ''),
		'HOST': os.getenv('DATABASE_HOST', ''),
		'PORT': os.getenv('DATABASE_PORT', ''),
	}
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'en-us')

TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')

USE_I18N = ast.literal_eval(os.getenv('USE_I18N', 'True'))

USE_L10N = ast.literal_eval(os.getenv('USE_L10N', 'True'))

USE_TZ = ast.literal_eval(os.getenv('USE_TZ', 'True'))


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = '/var/www/example.com/static/'
STATIC_ROOT = '/src/static-files'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, os.getenv('IMAGE_FOLDER', '/images/'))

CART_SESSION_ID = 'cart'

SITE_ID = 1

# Custom User Model
# https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#substituting-a-custom-user-model
#AUTH_USER_MODEL = 'customer.User'

# REST_FRAMEWORK
# https://www.django-rest-framework.org/
REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
		'rest_framework.permissions.IsAuthenticatedOrReadOnly',
	),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.SessionAuthentication',
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.TokenAuthentication',
		'rest_framework_simplejwt.authentication.JWTAuthentication',
	),
	# Json API
	# https://github.com/django-json-api/django-rest-framework-json-api
	'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
	'DEFAULT_PAGINATION_CLASS': 'rest_framework_json_api.pagination.JsonApiPageNumberPagination',
	#'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
	'DEFAULT_PARSER_CLASSES': (
		'rest_framework_json_api.parsers.JSONParser',
		'rest_framework.parsers.FormParser',
		'rest_framework.parsers.MultiPartParser'
	),
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework_json_api.renderers.JSONRenderer',
		'rest_framework.renderers.BrowsableAPIRenderer',
	),
	'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
	'DEFAULT_FILTER_BACKENDS': (
		'rest_framework_json_api.filters.QueryParameterValidationFilter',
		'rest_framework_json_api.filters.OrderingFilter',
		'rest_framework_json_api.django_filters.DjangoFilterBackend',
		'rest_framework.filters.SearchFilter',
	),
	'SEARCH_PARAM': 'filter[search]',
	'TEST_REQUEST_RENDERER_CLASSES': (
		'rest_framework.renderers.MultiPartRenderer',
		'rest_framework.renderers.JSONRenderer',
		'rest_framework_json_api.renderers.JSONRenderer',
		'rest_framework.renderers.TemplateHTMLRenderer',
	),
	'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json',
	'PAGE_SIZE': 20,
}

JSON_API_FORMAT_TYPES = 'dasherize'

# JWT
# https://github.com/davesque/django-rest-framework-simplejwt
SIMPLE_JWT = {
	'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
	'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

# CORS
# https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_WHITELIST = (
	'localhost:8000',
	'localhost:4200',
	'127.0.0.1:9000',
	'localhost'
)

# CKEDITOR
# https://django-ckeditor.readthedocs.io/en/latest/
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'Language'],
            ['Bold', 'Italic', 'Underline'],
            ['Styles', 'Format', 'Font', 'FontSize', 'TextColor', 'BGColor'],
            ['Link', 'Unlink'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'],
            ['Find', 'Replace', 'SelectAll'],
            ['RemoveFormat', 'Source'],
            ['Maximize', 'ShowBlocks'],
        ],
        'tabSpaces': 2,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            'autoembed',
            'embedsemantic',
            'autogrow',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
        'width': 850,
        'height': 200,
    },
}

# Faker
# https://faker.readthedocs.io/en/master/index.html
FAKER_LOCALIZATION=os.getenv('FAKER_LOCALIZATION', 'en_US')
