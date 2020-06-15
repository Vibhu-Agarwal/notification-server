from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from background_task import background
from rest_framework.generics import CreateAPIView, DestroyAPIView


class CreateNotificationAPIView(CreateAPIView):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = ()


class DeleteNotificationAPIView(DestroyAPIView):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = ()


@background()
def notify():
    print('WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
    return Response({})


class TestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        notify(schedule=90)
