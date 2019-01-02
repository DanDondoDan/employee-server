from rest_framework import serializers
from employee_server import models


class PersonPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = ('first_name',
                  'last_name',
                  'middle_name',
                  'position',
                  )


class PersonPrivateSerializer(PersonPublicSerializer):

    
    class Meta:
        model = models.Person
        fields = PersonPublicSerializer.Meta.fields + (
            'employment_date',
            'salary',
            'chief',
            'unit',
            )

    
