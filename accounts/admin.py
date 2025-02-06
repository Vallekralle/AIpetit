from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "first_name",
        "last_name",
        "email",
        "date_joined",
    ]
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("first_name", "last_name", "username", "email", "password1", "password2"),
        }),
    )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)