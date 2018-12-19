import logging

from rest_framework import serializers
from employee_server import models


logger = logging.getLogger(__name__)


class UserPublicSerializer(serializers.ModelSerializer):

    specialist = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Specialist.objects.all())
    
    class Meta:
        model = models.User
        fields = ('email', 'phone', 'birth', )



