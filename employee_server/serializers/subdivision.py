from rest_framework import serializers
from employee_server import models

class RecursiveField(serializers.Serializer):
    def to_native(self, value):
        return self.parent.to_native(value)


class SubdivisionSerializer(serializers.ModelSerializer):

    children = RecursiveField(many=True, required=False)
    full_name = serializers.ReadOnlyField(source='get_full_name')
    specialist_count = serializers.ReadOnlyField(source='get_specialist_count')
    low_level_manager_count = serializers.ReadOnlyField(source='get_low_level_manager_count')
    top_manager_count = serializers.ReadOnlyField(source='get_top_manager_count')
    senior_manager_count = serializers.ReadOnlyField(source='get_senior_manager_count')
    general_manager_count = serializers.ReadOnlyField(source='get_general_manager_count')
    stockholder_count = serializers.ReadOnlyField(source='get_stockholder_count')

    class Meta:
        model = models.Subdivision
        fields = ('id', 
                  'name',
                  'children',
                  'full_name',
                  'stockholder_count',
                  'general_manager_count',
                  'senior_manager_count',
                  'top_manager_count',
                  'low_level_manager_count',
                  'specialist_count',
                   )
