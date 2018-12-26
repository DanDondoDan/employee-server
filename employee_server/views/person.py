from rest_framework import viewsets as views
from employee_server import models
from employee_server import serializers


class PersonViewSet(views.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonPrivateSerializer
    
    