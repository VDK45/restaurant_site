from django.contrib import admin
from .models import *

# Register your models here.
# Добавить свое приложение в админку


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'updated_at', 'is_published')
    list_display_links = ('id', 'name', 'price', 'updated_at')
    search_fields = ('name', 'price')


admin.site.register(Menu, MenuAdmin)

