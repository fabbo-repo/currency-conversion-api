from pathlib import Path
from configurations import Configuration
import os
from django.utils.translation import gettext_lazy as _
import environ
from django.core.management.utils import get_random_secret_key


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    APP_DEBUG=(bool, os.getenv("APP_DEBUG", default=True)),
    APP_ALLOWED_HOSTS=(str, os.getenv("APP_ALLOWED_HOSTS", default='*')),
    APP_CORS_HOSTS=(str, os.getenv("APP_CORS_HOSTS")),
    DATABASE_URL=(str, os.getenv("DATABASE_URL",
                                 default='sqlite:///'+os.path.join(BASE_DIR, 'default.sqlite3'))),
    DEFAULT_API_KEY=(str, os.getenv("DEFAULT_API_KEY", default="")),
    CURRENCY_CODES=(str, os.getenv("CURRENCY_CODES", default='EUR,USD')),
    MAX_STORED_DAYS=(int, os.getenv("MAX_STORED_DAYS", default=20)),
    MAX_NO_UPDATED_MINS=(int, os.getenv("MAX_NO_UPDATED_MINS", default=60)),
)


class Dev(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    SECRET_KEY = get_random_secret_key()

    # True by default but have the option to set it false with an environment variable
    DEBUG = env('APP_DEBUG')

    ALLOWED_HOSTS = env('APP_ALLOWED_HOSTS').split(',')
    if env('APP_CORS_HOSTS'):
        CORS_ALLOW_ALL_ORIGINS = False
        CORS_ALLOWED_ORIGINS = env('APP_CORS_HOSTS').split(',')
    else:
        CORS_ALLOW_ALL_ORIGINS = True
    X_FRAME_OPTIONS = 'DENY'

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Cors:
        "corsheaders",
        # Rest framework:
        'rest_framework',
        'django_filters',
        # Cron jobs:
        'django_crontab',
        # Swager:
        'drf_yasg',
        # Custom apps:
        'core',
        'conversion',
        'currency',
        'api_key'
    ]

    MIDDLEWARE = [
        "corsheaders.middleware.CorsMiddleware",
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'core.urls'

    CSRF_FAILURE_VIEW = 'core.views.csrf_failure'

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

    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases
    DATABASES = {"default": env.db()}

    # Password validation
    # https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
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
    # https://docs.djangoproject.com/en/4.1/topics/i18n/
    LANGUAGE_CODE = 'en'
    LOCALE_PATHS = [
        BASE_DIR / 'locale/',
    ]
    LANGUAGES = (
        ('en', _('English')),
        ('es', _('Spanish')),
    )
    TIME_ZONE = "UTC"
    # Enables Django’s translation system
    USE_I18N = True
    # Django will display numbers and dates using the format of the current locale
    USE_L10N = True
    # Datetimes will be timezone-aware
    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/
    # (Statis url is not used in this project)
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / "static"

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "verbose",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        }
    }

    # Django Rest Framework setting:
    REST_FRAMEWORK = {
        "DEFAULT_PERMISSION_CLASSES": [
            "api_key.permissions.HasAPIKey"
        ],
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": 10,
        "DEFAULT_FILTER_BACKENDS": [
            "django_filters.rest_framework.DjangoFilterBackend",
        ],
        "DEFAULT_THROTTLE_CLASSES": [
            "rest_framework.throttling.AnonRateThrottle",
            "rest_framework.throttling.UserRateThrottle"
        ],
        "DEFAULT_THROTTLE_RATES": {
            "anon": "300/minute",
            "user": "300/minute",
        },
        'EXCEPTION_HANDLER': 'core.exceptions.app_exception_handler'
    }

    SWAGGER_SETTINGS = {
        "SECURITY_DEFINITIONS": {
            "API Key": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            },
        }
    }

    # Cron jobs (https://crontab.guru/)
    CRONJOBS = [
        ('0 */6 * * *', 'conversion.cron.update_currency_conversion')
    ]

    # Currency conversion settings

    CURRENCY_CODES = env('CURRENCY_CODES').split(',')
    DEFAULT_API_KEY = env('DEFAULT_API_KEY')
    # Maximum number of days to store a conversion
    MAX_STORED_DAYS = env('MAX_STORED_DAYS')
    # Maximum number of minutes to avoid updating a conversion
    MAX_NO_UPDATED_MINS = env('MAX_NO_UPDATED_MINS')


class OnPremise(Dev):
    DEBUG = False
    WSGI_APPLICATION = 'core.wsgi.application'

    # Security headers
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    if os.path.exists('/var/log/api/app.log'):
        print("* Using file log")
        LOGGING = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "verbose": {
                    "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
                    "style": "{",
                },
            },
            "handlers": {
                "logfile": {
                    "class": "logging.FileHandler",
                    "filename": "/var/log/api/app.log",
                    "formatter": "verbose",
                },
            },
            "root": {
                "handlers": ["logfile"],
                "level": "ERROR",
            }
        }
    else:
        print("* Using console log")
        LOGGING = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "verbose": {
                    "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
                    "style": "{",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "formatter": "verbose",
                },
            },
            "root": {
                "handlers": ["console"],
                "level": "ERROR",
            }
        }