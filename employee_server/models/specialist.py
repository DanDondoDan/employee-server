from django.db import models
from employee_server.models.base import BaseModel
from mptt.models import MPTTModel, TreeForeignKey

class Specialist(BaseModel):

    user = models.OneToOneField('User', on_delete=models.CASCADE,
                                related_name='%(class)s',
                                related_query_name='%(class)s'
                                )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    employment_date = models.DateField(default=None)
    salary = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    department = TreeForeignKey('Subdivision', null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default=None)

    def __str__(self):
        return "{} {} {} {} {} {} ({})".format(
            self.last_name, 
            self.first_name, 
            self.patronymic_name,
            self.position,
            self.employment_date,
            self.salary, 
            self.user.email
            )

    class Meta:
        verbose_name = 'Specialist'
        verbose_name_plural = 'Specialists'