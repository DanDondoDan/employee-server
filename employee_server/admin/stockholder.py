from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm
from employee_server.models.stockholder import Stockholder


class StockholderAdminForm(BaseForm):
    class Meta:
        model = models.Stockholder
        exclude = BaseForm.Meta.exclude

class  StockholderInline(admin.TabularInline):
    model = Stockholder.general_manager.through

@admin.register(models.Stockholder)
class TopManagerAdmin(admin.ModelAdmin):
    form = StockholderAdminForm
    list_display = ('last_name', 'first_name', 'patronymic_name', 'position', 'employment_date', 'salary', 
                    'get_general_manager', )

    inlines = (
        StockholderInline,
    )
    exclude = ('general_manager',)