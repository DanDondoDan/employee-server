from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from employee_server.models.specialist import Specialist
from employee_server.models.low_level_manager import LowLevelManager
from employee_server.models.top_manager import TopManager
from employee_server.models.senior_manager import SeniorManager
from employee_server.models.general_manager import GeneralManager
from employee_server.models.stockholder import Stockholder


class Subdivision(MPTTModel):
    
    id = models.CharField(
        max_length=32,
        primary_key=True,
        unique=True,
        verbose_name='ID',
        help_text='Forsquare ID of the subdivision.',
    )
    name = models.CharField(max_length=255, verbose_name= 'Name')

    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        db_index=True,
        verbose_name='Parent subdivision',
        help_text='Parent subdivision.',
        on_delete=models.CASCADE,
    )
    
    plural_name = models.CharField(
        max_length=255,
        verbose_name='Plural name'
    )

    class Meta:
        unique_together = (('parent',))
        verbose_name = 'Subdivision'
        verbose_name_plural = 'Subdivision'

    class MPTTMeta:
        order_insertion_by = ['name']
    
    def get_specialist_count(self):
        ids = self.get_descendants(include_self=True)
        return Specialist.objects.filter(department__in=ids).count()

    def __str__(self):
        return self.name