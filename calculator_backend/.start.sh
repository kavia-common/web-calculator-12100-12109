#!/bin/bash
# Entrypoint to run the Django server on all interfaces, port 3001 for cloud/preview usage.
set -e
cd "$(dirname "$0")"
exec python manage.py runserver 0.0.0.0:3001
