from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm
from mptt.admin import MPTTModelAdmin
from employee_server.models.subdivision import Subdivision



class SubdivisionAdminForm(BaseForm):
    class Meta:
        model = models.Subdivision
        exclude = BaseForm.Meta.exclude


@admin.register(models.Subdivision)
class SubdivisionAdmin(MPTTModelAdmin):
    form = SubdivisionAdminForm
    