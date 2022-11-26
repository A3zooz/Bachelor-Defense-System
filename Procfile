release: python manage.py migrate
api: gunicorn backend.wsgi --log-file -
web: npm start