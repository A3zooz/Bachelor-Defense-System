release: python manage.py migrate
api: gunicorn backend.backend.wsgi --log-file -
web: npm start