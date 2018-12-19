from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm
from employee_server.models.low_level_manager import LowLevelManager
from mptt.admin import MPTTModelAdmin


class LowLevelManagerAdminForm(BaseForm):
    class Meta:
        model = models.LowLevelManager
        exclude = BaseForm.Meta.exclude

class  LowLevelManagerInline(admin.TabularInline):
    model = LowLevelManager.specialist.through

@admin.register(models.LowLevelManager)
class LowLevelManagerAdmin(admin.ModelAdmin):
    form = LowLevelManagerAdminForm
    list_display = ('last_name', 'first_name', 'patronymic_name', 'position', 'employment_date', 'salary', 
                    'get_specialist', )

    inlines = (
        LowLevelManagerInline,
    )
    exclude = ('specialist',)
    mptt_indent_field = "some_node_field"