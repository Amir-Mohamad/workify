from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
	model = User
	list_display = ('email', 'last_name', 'is_active', 'is_staff', 'thumbnail')
	list_filter = ('is_active', 'is_staff', 'is_author')
	fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'avatar')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_author', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
	search_fields = ('email', 'last_name', 'first_name')
	ordering = ('email',)
