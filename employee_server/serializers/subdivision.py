from rest_framework import serializers
from employee_server import models
from rest_framework_recursive.fields import RecursiveField


class SubdivisionTreeSerializer(serializers.ModelSerializer):
    
    children = RecursiveField(many=True)
    specialist_count = serializers.ReadOnlyField(source='get_specialist_count')
   

    class Meta:
        model = models.Subdivision
        fields = ('id', 
                  'name',
                  'plural_name',
                  'children',
                  
                  'specialist_count',
                  )
           
