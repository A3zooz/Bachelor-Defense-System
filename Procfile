release: python manage.py migrate
web: gunicorn backend.wsgi --log-file -
web: npm start