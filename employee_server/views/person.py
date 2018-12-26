from rest_framework import viewsets as views
from employee_server import models
from employee_server import serializers

from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class PersonViewSet(views.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonPrivateSerializer

class SearchPersonViewSet(views.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonPrivateSerializer

    __basic_fields = ('first_name',
                      'last_name',
                      'position',
                      'employment_date',
                      'salary',
                      'chief',
                      'unit',
                      )
    
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    
    