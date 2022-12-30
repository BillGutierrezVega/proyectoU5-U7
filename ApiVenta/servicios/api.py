from rest_framework import viewsets, permissions

from servicios.models import ServicesMoldel
from servicios.serializers import ServicesSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = ServicesMoldel.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [permissions.AllowAny]