from rest_framework import viewsets, permissions

from usuarios.models import UserModel
from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny)