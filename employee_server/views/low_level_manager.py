from rest_framework import viewsets as views
from employee_server import models
from employee_server import serializers


class LowLevelManagerViewSet(views.ModelViewSet):
    queryset = models.LowLevelManager.objects.all()
    serializer_class = serializers.LowLevelManagerPrivateSerializer