from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm




class EmployeeAdminForm(BaseForm):
    class Meta:
        model = models.Employee
        exclude = BaseForm.Meta.exclude


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeAdminForm
    list_display = ('last_name', 'first_name', 'patronymic_name', 'position', 'employment_date', 'salary', )
                    