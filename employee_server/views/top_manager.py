from rest_framework import viewsets as views
from employee_server import models
from employee_server import serializers


class TopManagerViewSet(views.ModelViewSet):
    queryset = models.TopManager.objects.all()
    serializer_class = serializers.TopManagerPrivateSerializer