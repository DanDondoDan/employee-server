from rest_framework import serializers
from employee_server import models


class LowLevelManagerPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LowLevelManager
        fields = ('first_name', 'last_name', 'patronymic_name', 'position',)


class LowLevelManagerPrivateSerializer(LowLevelManagerPublicSerializer):

    email = serializers.SerializerMethodField()

    class Meta:
        model = models.LowLevelManager
        fields = LowLevelManagerPublicSerializer.Meta.fields + (
            'email',
            'employment_date',
            'salary',
            'department',
            )

    def get_email(self, obj: models.LowLevelManager):
        return obj.user.email