from django.contrib import admin
from .models import *

# Register your models here.
# Добавить свое приложение в админку


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'price', 'updated_at', 'is_published')
    list_display_links = ('id', 'category', 'name', 'price', 'updated_at')
    search_fields = ('name', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at')
    list_display_links = ('id', 'title', 'updated_at')
    search_fields = ('title',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)

