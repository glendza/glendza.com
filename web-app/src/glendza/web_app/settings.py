from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent

# Environment:
env = environ.Env()
env.prefix = "GLENDZA__"
env.read_env()

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG", False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# Application definition:

INSTALLED_APPS = [
    # Django apps:
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # TODO: Test app, remove later!
    "glendza.web_app.apps.testapp",
    # Main website app:
    # TODO
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "glendza.web_app.urls"

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

WSGI_APPLICATION = "glendza.web_app.wsgi.application"


# Database:
DB_LOCATION = env.str("DB_LOCATION", BASE_DIR / "db.sqlite3")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DB_LOCATION,
    }
}


# Password validation:
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


# Internationalization:
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files:
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = env.str("STATIC_ROOT", BASE_DIR / "staticfiles")


# Media files:
MEDIA_URL = "media/"
MEDIA_ROOT = env.str("MEDIA_ROOT", BASE_DIR / "media")


# Default auto field:
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
