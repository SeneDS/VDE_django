#!/bin/bash

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "🛠 Running migrations..."
python manage.py migrate

echo "🚀 Starting development server..."
exec "$@"
