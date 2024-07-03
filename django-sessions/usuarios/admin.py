from django.contrib import admin
from .models import User
from .forms import (
    UserChangeForm as AdminUserChangeForm,
    UserCreationForm as AdminUserCreationForm,
)
from django.contrib.auth.admin import UserAdmin as AdminUserAdmin


# admin.site.register(User)


@admin.register(User)
class UserAdmin(AdminUserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserCreationForm
    model = User
    fieldsets = AdminUserAdmin.fieldsets + (
        (
            ("extra-Infos"),
            {
                "fields": ("nick_name", "age", "specialy"),
            },
        ),
    )
