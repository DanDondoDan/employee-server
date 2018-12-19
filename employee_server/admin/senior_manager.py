from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm
from employee_server.models.senior_manager import SeniorManager


class SeniorManagerAdminForm(BaseForm):
    class Meta:
        model = models.SeniorManager
        exclude = BaseForm.Meta.exclude

class SeniorManagerInline(admin.TabularInline):
    model = SeniorManager.low_manager.through

@admin.register(models.SeniorManager)
class SubdivisionAdmin(admin.ModelAdmin):
    form = SeniorManagerAdminForm
    list_display = ('last_name', 'first_name', 'patronymic_name', 'position', 'employment_date', 'salary', 
                    'get_manager', )

    inlines = (
        SeniorManagerInline,
    )
    exclude = ('low_level_manager',)