from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm
from employee_server.models.top_manager import TopManager


class TopManagerAdminForm(BaseForm):
    class Meta:
        model = models.TopManager
        exclude = BaseForm.Meta.exclude

class  TopManagerInline(admin.TabularInline):
    model = TopManager.sub_manager.through

@admin.register(models.TopManager)
class TopManagerAdmin(admin.ModelAdmin):
    form = TopManagerAdminForm
    list_display = ('last_name', 'first_name', 'patronymic_name', 'position', 'employment_date', 'salary', 
                    'get_sub_manager', )

    inlines = (
        TopManagerInline,
    )
    exclude = ('sub_manager',)