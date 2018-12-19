from rest_framework import serializers
from employee_server import models


class StockholderPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Stockholder
        fields = ('first_name', 'last_name', 'patronymic_name', 'position',)


class StockholderPrivateSerializer(StockholderPublicSerializer):

    email = serializers.SerializerMethodField()

    class Meta:
        model = models.Stockholder
        fields = StockholderPublicSerializer.Meta.fields + (
            'email',
            'employment_date',
            'salary',
            'department',
            )

    def get_email(self, obj: models.Stockholder):
        return obj.user.email