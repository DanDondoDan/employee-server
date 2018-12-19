from rest_framework import viewsets as views
from employee_server import models
from employee_server import serializers


class StockholderViewSet(views.ModelViewSet):
    queryset = models.Stockholder.objects.all()
    serializer_class = serializers.StockholderPrivateSerializer