from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


METHOD_CHOICES = [
    ('post', 'POST'),
    ('delete', 'DELETE'),
    ('patch', 'PATCH'),
    ('get', 'GET')
]


class Notification(models.Model):

    url = models.URLField(null=False, blank=False)
    method = models.CharField(choices=METHOD_CHOICES, default='post', max_length=6)
    data = models.TextField(null=True)
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['time', 'created_at']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return f'{self.url} | {self.time}'
