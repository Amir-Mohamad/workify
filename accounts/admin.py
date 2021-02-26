from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from accounts.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
	model = User
	list_display = ('email', 'last_name', 'is_active', 'is_staff', 'thumbnail')
	list_filter = ('is_active', 'is_staff')
	fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
	search_fields = ('email', 'last_name', 'first_name')
	ordering = ('email',)
