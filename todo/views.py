from django.contrib.auth.models import User
from rest_framework.decorators import api_view, throttle_classes
from rest_framework import viewsets, serializers
from rest_framework.response import Response


class TodoViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    @staticmethod
    def hello():
        print('hello', flush=True)

    def list(self, request=None):
        # queryset = User.objects.all()
        # serializer = UserSerializer(queryset, many=True)
        return Response({})

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


@api_view(['GET'])
def hello(request=None):
    return Response({"message": "Hello for today! See you tomorrow!"})
