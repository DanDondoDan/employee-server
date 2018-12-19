from rest_framework import serializers
from employee_server import models


class SeniorManagerPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SeniorManager
        fields = ('first_name', 'last_name', 'patronymic_name', 'position',)


class SeniorManagerPrivateSerializer(SeniorManagerPublicSerializer):

    email = serializers.SerializerMethodField()

    class Meta:
        model = models.SeniorManager
        fields = SeniorManagerPublicSerializer.Meta.fields + (
            'email',
            'employment_date',
            'salary',
            'department',
            )

    def get_email(self, obj: models.SeniorManager):
        return obj.user.email