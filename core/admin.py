from django.contrib import admin
from . models import AboutUsModel, ContactUsModel


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('name',)


admin.site.register(AboutUsModel, AboutUsAdmin)
admin.site.register(ContactUsModel)