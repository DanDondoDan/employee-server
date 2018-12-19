from rest_framework import serializers
from employee_server import models


class SpecialistPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Specialist
        fields = ('first_name', 'last_name', 'patronymic_name', 'position',)


class SpecialistPrivateSerializer(SpecialistPublicSerializer):

    # email = serializers.SerializerMethodField()

    class Meta:
        model = models.Specialist
        fields = SpecialistPublicSerializer.Meta.fields + (
            'employment_date',
            'salary',
            'department',
            )

    # def get_email(self, obj: models.Specialist):
        # return obj.user.email