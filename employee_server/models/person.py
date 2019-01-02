from django.db import models
from mptt.models import TreeForeignKey
from employee_server.models.position import Position


class Person(models.Model):
    
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
            )

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Person'
