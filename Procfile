release: python manage.py migrate
api: gunicorn defense-scheduler.backend.wsgi --log-file -
web: npm start