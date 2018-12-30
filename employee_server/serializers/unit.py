from rest_framework import serializers
from employee_server import models
from rest_framework_recursive.fields import RecursiveField


class UnitTreeSerializer(serializers.ModelSerializer):

    children = RecursiveField(many=True)
    unit_count = serializers.ReadOnlyField(source='get_person_count')
   
    class Meta:
        model = models.Unit
        fields = ('id',
                  'name',
                  'plural_name',
                  'children',
                  'unit_count',
                  )


class UnitDetail(serializers.ModelSerializer):

    class Meta:
        model = models.Unit
        fields = ('id',
                  'name',
                  'plural_name',
                  'children',
                  )
