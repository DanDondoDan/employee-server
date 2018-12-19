from rest_framework import serializers
from employee_server import models


class GeneralManagerPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GeneralManager
        fields = ('first_name', 'last_name', 'patronymic_name', 'position',)


class GeneralManagerPrivateSerializer(GeneralManagerPublicSerializer):

    email = serializers.SerializerMethodField()

    class Meta:
        fields = GeneralManagerPublicSerializer.Meta.fields + (
            'employment_date',
            'salary',
            'department',
            )

    def get_email(self, obj: models.GeneralManager):
        return obj.user.email