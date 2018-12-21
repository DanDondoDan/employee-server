from rest_framework import viewsets as views
from employee_server import models
from employee_server import serializers
from employee_server.models.subdivision import Subdivision
from mptt.templatetags.mptt_tags import cache_tree_children
from rest_framework.response import Response


class SubdivisionViewSet(views.ModelViewSet):

    queryset = models.Subdivision.objects.all()
    serializer_class = serializers.SubdivisionSerializer

    def specialist_list(self, request):
        tree = cache_tree_children(Subdivision.objects.filter(level=0))
        serializer = serializers.SubdivisionSerializer(tree, many=True)
        return Response(serializer.data) 