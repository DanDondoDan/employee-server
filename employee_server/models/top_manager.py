from django.db import models
from employee_server.models.base import BaseModel
from employee_server.models.subdivision_manager import SubdivisionManager


class TopManager(BaseModel):

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

    sub_manager = models.ManyToManyField(SubdivisionManager, related_name='sub_manager')

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

    def get_sub_manager(self):
        return ",".join([str(p) for p in self.sub_manager.all()])

    get_sub_manager.short_description = "Subdivision Manager"

    class Meta:
        verbose_name = 'Top Manager'
        verbose_name_plural = 'Top Managers'