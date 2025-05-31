#!/bin/sh
# set -e

# Collect static files
echo "Starting collectstatic"
gmanage collectstatic --no-input

# Run migrations
echo "Starting migrate"
gmanage migrate --noinput

exec "$@"
