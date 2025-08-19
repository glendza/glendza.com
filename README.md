# Glendza - Web App

## Development

### Project setup

Install dependencies using uv:

```sh
uv sync --extra dev
```

## Environment variables

| Key | Required | Default| Description |
| ------------- | ------------- | ------------- | ------------- |
| **GLENDZA__DEBUG** | ❌ | False | Enables or disables debugging. Set to 'True' for debugging mode. |
| **GLENDZA__SECRET_KEY** | ✅ | N/A | The secret key used for cryptographic operations in Django. |
| **GLENDZA__ALLOWED_HOSTS** | ✅ | N/A | A list of allowed hostnames or IP addresses for the Django app. |
| **GLENDZA__DB_LOCATION** | ❌ | N/A | Path to the SQLite database file used by the Django application. |
| **GLENDZA__STATIC_URL** | ❌ | /static/ | URL prefix for serving static files. |
| **GLENDZA__STATIC_ROOT** | ❌ | N/A | Directory where static files are collected for serving in production. |
| **GLENDZA__MEDIA_URL** | ❌ | /media/ | URL prefix for serving media files. |
| **GLENDZA__MEDIA_ROOT** | ❌ | N/A | Directory for storing user-uploaded media files. |
| **GLENDZA__DJANGO_ADMIN_URL** | ❌ | admin/ | URL path for Django admin interface. |
| **GLENDZA__WAGTAIL_ADMIN_URL** | ❌ | cms/ | URL path for Wagtail CMS admin interface. |
| **GLENDZA__EMAIL_BACKEND** | ❌ | django.core.mail.backends.smtp.EmailBackend | Email backend to use for sending emails. |
| **GLENDZA__EMAIL_HOST** | ✅ | N/A | SMTP server hostname for sending emails. |
| **GLENDZA__EMAIL_PORT** | ❌ | 587 | SMTP server port for sending emails. |
| **GLENDZA__EMAIL_USE_TLS** | ❌ | True | Whether to use TLS encryption for SMTP connection. |
| **GLENDZA__EMAIL_HOST_USER** | ✅ | N/A | SMTP username for authentication. |
| **GLENDZA__EMAIL_HOST_PASSWORD** | ✅ | N/A | SMTP password or app password for authentication. |
| **GLENDZA__EMAIL_USE_SSL** | ❌ | False | Whether to use SSL encryption for SMTP connection. |
| **GLENDZA__RECAPTCHA_PUBLIC_KEY** | ✅ | N/A | Public key for Google reCAPTCHA integration. |
| **GLENDZA__RECAPTCHA_PRIVATE_KEY** | ✅ | N/A | Private key for Google reCAPTCHA integration. |
| **GLENDZA__LOG_LEVEL** | ❌ | INFO | Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL). |
| **GLENDZA__LOG_LOCATION** | ✅ | N/A | Directory where log files will be stored. |
