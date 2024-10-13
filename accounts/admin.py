from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role, Branch

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'role', 'branch', 'is_staff', 'is_active']
    list_filter = ['email', 'is_staff', 'is_active', 'role', 'branch']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Role and Branch', {'fields': ('role', 'branch')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active', 'role', 'branch')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Role)
admin.site.register(Branch)
