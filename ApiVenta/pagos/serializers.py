from rest_framework import serializers

from pagos.models import PaymentUserModel, ExpiredPaymentsModel


class PagadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentUserModel
        fields = '__all__'
        

class ExpiradosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiredPaymentsModel
        fields = '__all__'