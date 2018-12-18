from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm
from employee_server.models.manager import Manager
from mptt.admin import MPTTModelAdmin


class ManagerAdminForm(BaseForm):
    class Meta:
        model = models.Manager
        exclude = BaseForm.Meta.exclude

class  ManagerInline(admin.TabularInline):
    model = Manager.employee.through

@admin.register(models.Manager)
class ManagerAdmin(admin.ModelAdmin):
    form = ManagerAdminForm
    list_display = ('last_name', 'first_name', 'patronymic_name', 'position', 'employment_date', 'salary', 
                    'get_employee', )

    inlines = (
        ManagerInline,
    )
    exclude = ('employee',)
    mptt_indent_field = "some_node_field"