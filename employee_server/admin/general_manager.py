from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm
from employee_server.models.general_manager import GeneralManager


class GeneralManagerAdminForm(BaseForm):
    class Meta:
        model = models.GeneralManager
        exclude = BaseForm.Meta.exclude

class  GeneralManagerInline(admin.TabularInline):
    model = GeneralManager.top_manager.through

@admin.register(models.GeneralManager)
class TopManagerAdmin(admin.ModelAdmin):
    form = GeneralManagerAdminForm
    list_display = ('last_name', 'first_name', 'patronymic_name', 'position', 'employment_date', 'salary', 
                    'get_top_manager', )

    inlines = (
        GeneralManagerInline,
    )
    exclude = ('top_manager',)