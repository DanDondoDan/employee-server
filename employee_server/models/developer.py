from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Developer(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    # slug = models.SlugField(max_length=250)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = (('parent',))
        verbose_name_plural = 'staffs'

    def __str__(self):
        return self.name