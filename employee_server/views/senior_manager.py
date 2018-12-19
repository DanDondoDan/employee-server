from rest_framework import viewsets as views
from employee_server import models
from employee_server import serializers


class SeniorManagerViewSet(views.ModelViewSet):
    queryset = models.SeniorManager.objects.all()
    serializer_class = serializers.SeniorManagerPrivateSerializer