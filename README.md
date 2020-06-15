# notification-server
A server to make HTTP requests at a particular time with a database-backed work queue

## Configure Environment Variables (Heroku)
```
NOTIFICATIONS_SUPERUSER_PASSWORD=<ADMIN_PANEL_PASSWORD>
DISABLE_COLLECTSTATIC=1
```
**Username: `superuser`**

## Install Necessary Libraries
```bash
pip install gunicorn django-heroku
```

### Create `Procfile`
```
web: gunicorn notification_server.wsgi --bind 0.0.0.0:$PORT
release: python manage.py migrate && python manage.py db_setup
worker: python manage.py process_tasks
```

## Endpoints

### User & Authentication (`notifications/`)

| Method | Endpoint | Function |
|--|--|--|
| POST | `place/` | Place a new Notification |
| DELETE | `remove/<notification_id>` | Delete Notification with specified ID |
