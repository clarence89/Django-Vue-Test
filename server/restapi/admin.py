from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Animal

# Register your models here.
class CustomUserAdmin(UserAdmin):
        filter_horizontal = ('animals',)
        list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'colour'
        )

        fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Additional info', {
            'fields': ('colour','animals')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })

    )

        add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Additional info', {
            'fields': ('colour', 'animals')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
        )

admin.site.register(Animal)
admin.site.register(CustomUser,CustomUserAdmin)
