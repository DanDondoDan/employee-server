from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from employee_server.models.person import Person


class Unit(MPTTModel):
    
    id = models.CharField(
        max_length=32,
        primary_key=True,
        unique=True,
        verbose_name='ID',
        help_text='Forsquare ID of the unit.',
    )
    name = models.CharField(max_length=255, verbose_name= 'Name')

    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        db_index=True,
        verbose_name='Parent unit',
        help_text='Parent unit.',
        on_delete=models.CASCADE,
    )
    
    plural_name = models.CharField(
        max_length=255,
        verbose_name='Plural name'
    )

    class Meta:
        unique_together = (('parent',))
        verbose_name = 'Unit'
        verbose_name_plural = 'Unit'

    class MPTTMeta:
        order_insertion_by = ['name']
    
    def get_person_count(self):
        ids = self.get_descendants(include_self=True)
        return Person.objects.filter(unit__in=ids).count()

    def __str__(self):
        return self.name