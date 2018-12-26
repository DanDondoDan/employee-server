from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm




class PersonAdminForm(BaseForm):
    class Meta:
        model = models.Person
        exclude = BaseForm.Meta.exclude


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    form = PersonAdminForm
    list_display = ('last_name',
                    'first_name',
                    'middle_name',
                    'position',
                    'employment_date',
                    'salary',
                    'chief',
                    'unit',
                    )
                    