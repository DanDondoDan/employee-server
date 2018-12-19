from rest_framework import viewsets as views
from employee_server import models
from employee_server import serializers


class GeneralManagerViewSet(views.ModelViewSet):
    queryset = models.GeneralManager.objects.all()
    serializer_class = serializers.GeneralManagerPrivateSerializer