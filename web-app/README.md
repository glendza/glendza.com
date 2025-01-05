# Glendza - Web App

## Development

### Project setup

Install the package in development mode:

```sh
pip install -e .[dev]
```

Run the database migrations:

```sh
gmanage migrate
```

Collect staticfiles:

```sh
gmanage collectstatic --no-input
```

Run the application:

```sh
gmanage runserver 8123
```

## Environment variables

| Key | Required | Default| Description |
| ------------- | ------------- | ------------- | ------------- |
| **GLENDZA__DEBUG** | ❌ | False | Enables or disables debugging. Set to 'True' for debugging mode. |
| **GLENDZA__SECRET_KEY** | ✅ | N/A | The secret key used for cryptographic operations in Django. |
| **GLENDZA__DB_LOCATION** | ❌ | ./web-app/src/glendza/web-app/db.sqlite3 | Path to the SQLite database file used by the Django application.|
| **GLENDZA__ALLOWED_HOSTS** | ✅ | N/A | A list of allowed hostnames or IP addresses for the Django app. |
| **GLENDZA__STATIC_ROOT** | ❌ | ./web-app/src/glendza/web-app/staticfiles | Directory where static files are collected for serving in production. |
| **GLENDZA__MEDIA_ROOT** | ❌ | ./web-app/src/glendza/web-app/media | Directory for storing user-uploaded media files. |
