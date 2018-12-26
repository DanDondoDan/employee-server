from rest_framework import viewsets as views
from employee_server import models
from employee_server import serializers
# from employee_server.models.subdivision import Subdivision
from mptt.templatetags.mptt_tags import cache_tree_children
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import decorators
from rest_framework import generics
from employee_server.models.unit import Unit

from django.shortcuts import get_object_or_404
from oscar.core.loading import get_model
from rest_framework import generics

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
        

class UnitDetail(generics.RetrieveAPIView):
    queryset = Unit.objects.all()
    serializer_class = serializers.UnitDetail
  


##############################################################
Unit = get_model('employee_server', 'Unit')
Person = get_model('employee_server', 'Person')

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
    
        
