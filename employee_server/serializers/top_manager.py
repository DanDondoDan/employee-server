from rest_framework import serializers
from employee_server import models


class TopManagerPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TopManager
        fields = ('first_name', 'last_name', 'patronymic_name', 'position',)


class TopManagerPrivateSerializer(TopManagerPublicSerializer):

    email = serializers.SerializerMethodField()

    class Meta:
        model = models.TopManager
        fields = TopManagerPublicSerializer.Meta.fields + (
            'email',
            'employment_date',
            'salary',
            'department',
            )

    def get_email(self, obj: models.TopManager):
        return obj.user.email