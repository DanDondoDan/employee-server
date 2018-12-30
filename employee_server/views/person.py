from rest_framework import viewsets as views
from rest_framework import status
from employee_server import models
from employee_server import serializers
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import generics
from employee_server.decorators.decorators import validate_request_data


class SearchPersonViewSet(views.ModelViewSet):

    """
    GET person/
    POST person/
    filter/search person/
    """
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


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET person/:id/
    PUT person/:id/
    DELETE person/:id/
    """
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonPrivateSerializer

    def get(self, request, *args, **kwargs):
        try:
            pers = self.queryset.get(pk=kwargs["pk"])
            return Response(serializers.PersonPrivateSerializer(pers).data)
        except models.Person.DoesNotExist:
            return Response(
                data={
                    "message": "Person with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            pers = self.queryset.get(pk=kwargs["pk"])
            serializer = serializers.PersonPrivateSerializer
            updated_person = serializer.update(pers, request.data)
            return Response(serializers.PersonPrivateSerializer(updated_person).data)
        except models.Person.DoesNotExist:
            return Response(
                data={
                    "message": "Person with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            pers = self.queryset.get(pk=kwargs["pk"])
            pers.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Person.DoesNotExist:
            return Response(
                data={
                    "message": "Person with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
