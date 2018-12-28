from django.db import models
from employee_server.models.base import BaseModel
from mptt.models import MPTTModel, TreeForeignKey
from employee_server.models.position import Position


class Person(BaseModel):

    user = models.OneToOneField('User', on_delete=models.CASCADE,
                                related_name='%(class)s',
                                related_query_name='%(class)s'
                                )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)

    position = models.ForeignKey(Position, blank='True', null='True', on_delete=models.CASCADE)

    employment_date = models.DateField(default=None)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    chief = models.ForeignKey('self', blank='True', null='True', on_delete=models.CASCADE)
    unit = TreeForeignKey('Unit', null=True, blank=True, on_delete=models.CASCADE)

    photo = models.ImageField(blank=True, null=True, default=None, upload_to='media')
   
    def __str__(self):
        return "{} {} {} {} {} {} {} {} ({})".format(
            self.last_name, 
            self.first_name, 
            self.middle_name,
            self.position,
            self.employment_date,
            self.salary,
            self.chief,
            self.unit,
            self.photo, 
            self.user.email
            )

    # def get_positions(self):
        # return ",".join([str(p) for p in self.position.all()])

    # get_positions.short_description = "Positions"

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Person'