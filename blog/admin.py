from django.contrib import admin
from .models import Article, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','is_active')
    list_editable = ('is_active',)
    list_filter = ('name',)
    prepopulated_fields = {'slug', ('name',)}

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active', 'title', 'promote')
    list_editable = ('is_active','promote')
    prepopulated_fields = {'slug', ('title',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)