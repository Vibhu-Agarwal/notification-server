import json
import requests
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from background_task import background
from rest_framework.generics import DestroyAPIView

REQUEST_FUNCTIONS = {
    'post': requests.post,
    'delete': requests.delete,
    'patch': requests.patch,
    'get': requests.get
}

@background()
def notify(notification_id):
    notifications = Notification.objects.filter(id=notification_id)
    if notifications.exists():
        notification = notifications.first()
        fn = REQUEST_FUNCTIONS.get(notification.method)
        if notification.method in REQUEST_FUNCTIONS:
            if notification.method in ['post', 'patch']:
                data = notification.data
                if data is None:
                    data = '{}'
                fn(notification.url, data=data)
            elif notification.method in ['get', 'delete']:
                fn(notification.url)
            notification.delete()


class CreateNotificationAPIView(APIView):

    permission_classes = ()

    def post(self, request, *args, **kwargs):
        request_body = request.data
        data = request_body.get('data', None)
        if data:
            data = json.dumps(data)
        request_body.update({'data': data})
        notification_serializer = NotificationSerializer(data=request_body)
        notification_serializer.is_valid(raise_exception=True)
        notification = notification_serializer.save()
        notify(notification.id, schedule=notification.time)
        return Response(notification_serializer.data)


class DeleteNotificationAPIView(DestroyAPIView):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = ()
