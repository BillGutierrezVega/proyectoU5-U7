from rest_framework import serializers

from servicios.models import ServicesMoldel


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesMoldel
        fields = (
            'id',
            'name',
            'descripcion',
            'logo',
        )
        read_only_fields = ('id',)
