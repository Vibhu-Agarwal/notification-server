from .views import (CreateNotificationAPIView, DeleteNotificationAPIView)

from django.urls import path

app_name = 'notifications'

urlpatterns = [
    path('place/', CreateNotificationAPIView.as_view(), name='place_notification'),
    path('remove/<int:pk>', DeleteNotificationAPIView.as_view(), name='remove_notification'),
]