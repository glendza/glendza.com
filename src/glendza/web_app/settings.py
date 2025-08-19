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
    # Wagtail:
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.settings",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.contrib.routable_page",
    "wagtail",
    # Wagtail - third party:
    "taggit",
    "modelcluster",
    "django_recaptcha",
    "wagtailcaptcha",
    # Django apps:
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "glendza.web_app.apps.user",
    # Main website app:
    "glendza.web_app.apps.core",
    # Third party apps:
    "django_icons",
]

if DEBUG:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Wagtail:
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

if DEBUG:
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *MIDDLEWARE,
    ]

ROOT_URLCONF = "glendza.web_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "glendza.web_app.wsgi.application"


# Database:
DB_LOCATION = env.str("DB_LOCATION")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DB_LOCATION,
    }
}

# User model:
AUTH_USER_MODEL = "user.User"


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
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_URL = env.str("STATIC_URL", "/static/")
STATIC_ROOT = env.str("STATIC_ROOT")


# Media files:
MEDIA_URL = env.str("MEDIA_URL", "/media/")
MEDIA_ROOT = env.str("MEDIA_ROOT")

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "OPTIONS": {
            "location": MEDIA_ROOT,
        },
    },
    # Whitenoise - enable caching / compression:
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Default auto field:
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Django Admin:
DJANGO_ADMIN_URL = env.str("DJANGO_ADMIN_URL", "admin/")


# Django debug toolbar:
INTERNAL_IPS = [
    "127.0.0.1",
]

# Email settings:
EMAIL_BACKEND = env.str("EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend")
EMAIL_HOST = env.str("EMAIL_HOST")
EMAIL_PORT = env.int("EMAIL_PORT", 587)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", True)
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", False)

# Recaptcha settings:
RECAPTCHA_PUBLIC_KEY = env.str("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env.str("RECAPTCHA_PRIVATE_KEY")
NOCAPTCHA = True

# Wagtail settings:

WAGTAIL_ADMIN_URL = env.str("WAGTAIL_ADMIN_URL", "cms/")
WAGTAILADMIN_BASE_URL = f"http://127.0.0.1:8123/{WAGTAIL_ADMIN_URL}"  # TODO
WAGTAIL_SITE_NAME = "Glendza"
WAGTAILDOCS_EXTENSIONS = ["csv", "docx", "key", "odt", "pdf", "pptx", "rtf", "txt", "xlsx", "zip"]


# Reverse the default case-sensitive handling of tags:
TAGGIT_CASE_INSENSITIVE = True


# django-icons:

DJANGO_ICONS = {
    "ICONS": {
        "edit": {"name": "fa-solid fa-pencil"},
        "bars": {"name": "fa-solid fa-bars"},
        "xmark": {"name": "fa-solid fa-xmark"},
    },
}

# Logging configuration:
LOG_LEVEL = env.str("LOG_LEVEL", "INFO")
LOG_LOCATION = Path(env.str("LOG_LOCATION"))

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": LOG_LEVEL,
            "class": "logging.FileHandler",
            "filename": LOG_LOCATION / "glendza.log",
            "formatter": "verbose",
        },
        "console": {
            "level": LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": LOG_LEVEL,
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "wagtail": {
            "handlers": ["console", "file"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "glendza": {
            "handlers": ["console", "file"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    },
}
