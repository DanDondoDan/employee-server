from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from employee_server.models.specialist import Specialist
from employee_server.models.low_level_manager import LowLevelManager
from employee_server.models.top_manager import TopManager
from employee_server.models.senior_manager import SeniorManager
from employee_server.models.general_manager import GeneralManager
from employee_server.models.stockholder import Stockholder


class Subdivision(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(default=None)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = (('slug', 'parent',))
        verbose_name_plural = 'Subdivision'

    def get_full_name(self):
        names = self.get_ancestors(include_self=True).values('name')
        full_name = ' - '.join(map(lambda x: x['name'], names))
        return full_name
    
    def get_specialist_count(self):
        ids = self.get_descendants(include_self=True)
        return Specialist.objects.filter(department__in=ids).count()
    
    def get_low_level_manager_count(self):
        ids = self.get_descendants(include_self=True)
        return LowLevelManager.objects.filter(department__in=ids).count()

    def get_top_manager_count(self):
        ids = self.get_descendants(include_self=True)
        return TopManager.objects.filter(department__in=ids).count()
    
    def get_senior_manager_count(self):
        ids = self.get_descendants(include_self=True)
        return SeniorManager.objects.filter(department__in=ids).count()

    def get_general_manager_count(self):
        ids = self.get_descendants(include_self=True)
        return GeneralManager.objects.filter(department__in=ids).count()
    
    def get_stockholder_count(self):
        ids = self.get_descendants(include_self=True)
        return GeneralManager.objects.filter(department__in=ids).count()


    

    def __str__(self):
        return self.name