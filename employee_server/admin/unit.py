from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm
from mptt.admin import MPTTModelAdmin
from employee_server.models.unit import Unit


class UnitAdminForm(BaseForm):
    class Meta:
        model = models.Unit
        exclude = BaseForm.Meta.exclude


@admin.register(models.Unit)
class UnitAdmin(MPTTModelAdmin):
    form = UnitAdminForm
