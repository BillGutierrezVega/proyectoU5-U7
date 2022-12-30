from rest_framework import viewsets, permissions

from pagos.serializers import PagadosSerializer, ExpiradosSerializer
from pagos.models import PaymentUserModel, ExpiredPaymentsModel


class PagosHechosViewSet(viewsets.ViewSet):
    queryset = PaymentUserModel.objects.all()
    serializer_class = PagadosSerializer
    permission_classes = [permissions.AllowAny]

class PagosExpiradosViewSet(viewsets.ViewSet):
    queryset = ExpiredPaymentsModel.objects.all()
    serializer_class = ExpiradosSerializer
    permission_classes = [permissions.AllowAny]   
