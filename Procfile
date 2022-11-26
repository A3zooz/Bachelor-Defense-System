release: python manage.py migrate
worker: gunicorn defense-scheduler.backend.wsgi --log-file -
web: npm start