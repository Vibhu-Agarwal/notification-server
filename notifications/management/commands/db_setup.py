from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

email_superuser = 'vibhu4agarwal@gmail.com'
superuser_username = 'superuser'

help_message = f"""
Sets up the DB, creating:
1) superuser with admin rights (Email: {email_superuser})
"""


class Command(BaseCommand):
    """
    db_setup: Command to set-up database for the application
    """
    help = help_message

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username=superuser_username).exists():
            User.objects.create_superuser(username=superuser_username,
                                          first_name="Super User",
                                          email=email_superuser,
                                          password=settings.SUPERUSER_PASSWORD)
            print('Super-User Created!')
        print('Notification-Server DB Set-Up Complete!')
