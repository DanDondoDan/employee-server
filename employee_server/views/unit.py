from rest_framework import viewsets as views
from employee_server import serializers
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import decorators
from rest_framework import generics
from django.shortcuts import get_object_or_404
from employee_server.models.unit import Unit
from employee_server.models.person import Person


class UnitViewSet(
        mixins.ListModelMixin,
        views.GenericViewSet
        ):

    queryset = Unit.objects.all()
    serializer_class = serializers.UnitTreeSerializer
    pagination_class = None

    @decorators.list_route(methods=['get'])
    def tree(self, *args, **kwargs):

        categories = Unit.objects.filter(level=0).all()
        serializer = serializers.UnitTreeSerializer(categories, many=True)
        return Response(data=serializer.data)


class UnitEmployeerView(generics.ListAPIView):
    serializer_class = serializers.PersonPrivateSerializer

    def get_queryset(self):
        sub_id = self.kwargs.get('pk', None)
        if sub_id is not None:
            subdiv = get_object_or_404(Unit, id=sub_id)
            return Person.objects.filter(
                unit__in=subdiv.id).all()
        else:
            return Person.objects.none()
