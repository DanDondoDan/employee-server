from django.contrib import admin
from employee_server import models
from employee_server.admin.base import BaseForm
import django.forms as forms


class UserAdminForm(BaseForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('email', 'password', 'phone', 'birth')


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm