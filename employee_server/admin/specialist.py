from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm




class SpecialistAdminForm(BaseForm):
    class Meta:
        model = models.Specialist
        exclude = BaseForm.Meta.exclude


@admin.register(models.Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    form = SpecialistAdminForm
    list_display = ('last_name', 'first_name', 'patronymic_name', 'position', 'employment_date', 'salary', )
                    