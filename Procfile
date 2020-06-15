web: gunicorn notification_server.wsgi --bind 0.0.0.0:$PORT
release: python manage.py migrate && python manage.py db_setup
worker: python manage.py process_tasks
