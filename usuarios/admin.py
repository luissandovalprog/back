from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Añade el campo 'rol' al list_display y al fieldset
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'rol')
    fieldsets = UserAdmin.fieldsets + (
        ('Roles', {'fields': ('rol',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('rol',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)