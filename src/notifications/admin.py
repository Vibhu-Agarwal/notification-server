from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'method', 'time')
    list_display_links = ('id', 'url', 'method', 'time')


admin.site.register(Notification, NotificationAdmin)
