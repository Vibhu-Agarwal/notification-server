# notification-server
A server to make HTTP requests at a particular time with a database-backed work queue

## Fork and Clone
```bash
git clone https://github.com/<your-GitHub-Username>/notification-server.git
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Configure Environment Variables
```bash
export NOTIFICATIONS_SUPERUSER_PASSWORD="ADMIN_PANEL_PASSWORD"
```

## Configure Settings
(`src/notification_server/settings.py`)

Set `DELETE_PAST_NOTIFICATIONS` to `False` if you want to keep the past notifications' data in the DB
```python
DELETE_PAST_NOTIFICATIONS = True
```

## Create Admin User
```bash
cd src/
python manage.py db_setup
```
**Username: `superuser`**

## Usage
Run these two processes: Django-Server and `process_tasks` management command

### Running Locally

#### Django Server
```bash
python manage.py runserver
```
#### `process_tasks` Management Command
```bash
python manage.py process_tasks
```

## Endpoints

### User & Authentication (`notifications/`)

| Method | Endpoint | Function |
|--|--|--|
| POST | `place/` | Place a new Notification |
| DELETE | `remove/<notification_id>` | Delete Notification with specified ID |

#### `notifications/place/`
```json
{
  "url": STRING,
  "method": ["post"|"delete"|"patch"|"get"],
  "time": STRING,
  "data": JSON
}
```
**`time`**: [(Date and Time in proper format)](https://docs.djangoproject.com/en/3.0/ref/settings/#datetime-input-formats)