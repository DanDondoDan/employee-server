from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm
from employee_server.models.subdivision_manager import SubdivisionManager


class SubdivisionManagerAdminForm(BaseForm):
    class Meta:
        model = models.SubdivisionManager
        exclude = BaseForm.Meta.exclude

class  SubdivisionManagerInline(admin.TabularInline):
    model = SubdivisionManager.manager.through

@admin.register(models.SubdivisionManager)
class SubdivisionAdmin(admin.ModelAdmin):
    form = SubdivisionManagerAdminForm
    list_display = ('last_name', 'first_name', 'patronymic_name', 'position', 'employment_date', 'salary', 
                    'get_manager', )

    inlines = (
        SubdivisionManagerInline,
    )
    exclude = ('manager',)