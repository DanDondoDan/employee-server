from rest_framework import viewsets as views
from employee_server import models
from employee_server import serializers


class SpecialistViewSet(views.ModelViewSet):
    queryset = models.Specialist.objects.all()
    serializer_class = serializers.SpecialistPrivateSerializer