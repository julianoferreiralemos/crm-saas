from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'tenant', 'is_active', 'is_staff']
    list_filter = ['is_active', 'is_staff', 'tenant']
    fieldsets = UserAdmin.fieldsets + (
        ('Tenant', {'fields': ('tenant',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Tenant', {'fields': ('tenant',)}),
    )
