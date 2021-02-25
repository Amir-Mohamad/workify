from django.contrib import admin
from . models import AboutUsModel

class AboutUsAdmin(admin.ModelAdmin):
    list_editable = ('name',)
    list_filter = ('name',)

admin.site.register(AboutUsModel, AboutUsAdmin)