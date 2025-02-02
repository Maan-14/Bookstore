from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_superuser",
    ]
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = (
        None, 
        {
        "classes": ("wide",),
        "fields": ("username", "password1", "password2", "email", "is_superuser", "is_active"),
        }
    ),




admin.site.register(CustomUser, CustomUserAdmin)