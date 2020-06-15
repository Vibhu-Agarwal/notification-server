from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.generics import CreateAPIView, DestroyAPIView


class CreateNotificationAPIView(CreateAPIView):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = ()


class DeleteNotificationAPIView(DestroyAPIView):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = ()
