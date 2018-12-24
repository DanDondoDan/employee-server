from rest_framework import viewsets as views
from employee_server import models
from employee_server import serializers
from employee_server.models.subdivision import Subdivision
from mptt.templatetags.mptt_tags import cache_tree_children
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import decorators
from rest_framework import generics

from django.shortcuts import get_object_or_404
from oscar.core.loading import get_model
from rest_framework import generics

class SubdivisionViewSet(
        mixins.ListModelMixin,
        views.GenericViewSet
    ):
    
    queryset = Subdivision.objects.all()
    serializer_class = serializers.SubdivisionTreeSerializer
    pagination_class = None

    @decorators.list_route(methods=['get'])
    def tree(self, *args, **kwargs):
    
        categories = Subdivision.objects.filter(level=0).all()
        serializer = serializers.SubdivisionTreeSerializer(categories, many=True)
        return Response(data=serializer.data)

class SubDetail(generics.RetrieveAPIView):
    queryset = Subdivision.objects.all()
    serializer_class = serializers.SubDetail


##############################################################
Subdivision = get_model('employee_server', 'Subdivision')
Specialist = get_model('employee_server', 'Specialist')


class SubEmployeerView(generics.ListAPIView):
    serializer_class = serializers.SpecialistPrivateSerializer

    def get_queryset(self):
        sub_id = self.kwargs.get('pk', None)
        if sub_id is not None:
            subdiv = get_object_or_404(Subdivision, id=sub_id)
            return Specialist.objects.filter(
                department__in=subdiv.id).all()
        else:
            return Specialist.objects.none()
