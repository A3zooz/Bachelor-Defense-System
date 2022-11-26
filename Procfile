release: python manage.py migrate
api: gunicorn defense-scheduler.backend.backend.wsgi --log-file -
web: npm start