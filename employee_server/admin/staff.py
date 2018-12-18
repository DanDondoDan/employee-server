from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm
from mptt.admin import MPTTModelAdmin
from employee_server.models.staff import Staff



class StaffAdminForm(BaseForm):
    class Meta:
        model = models.Staff
        exclude = BaseForm.Meta.exclude


@admin.register(models.Staff)
class EmployeeAdmin(MPTTModelAdmin):
    form = StaffAdminForm
    