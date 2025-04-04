#!/bin/bash

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "🛠 Running migrations..."
python manage.py migrate

echo "🚀 Starting development server 0.0.0.0:8005 ..."
exec python manage.py runserver 0.0.0.0:8005