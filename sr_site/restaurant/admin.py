from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

# Register your models here.
# Добавить свое приложение в админку


class MenuAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Menu


class MenuAdmin(admin.ModelAdmin):
    form = MenuAdminForm
    list_display = ('id', 'category', 'name', 'price', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'name', 'price')
    search_fields = ('name', 'price')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('category', 'description', 'name', 'price', 'photo', 'get_photo', 'updated_at', 'is_published')
    readonly_fields = ('updated_at', 'get_photo')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'No photo'

    get_photo.short_description = 'Ảnh nhỏ'


admin.site.register(Menu, MenuAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at')
    list_display_links = ('id', 'title', 'updated_at')
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)


class ListGames(admin.ModelAdmin):
    list_display = ('name', 'photo', 'updated_at')
    list_display_links = ('name', 'photo', 'updated_at')
    search_fields = ('name',)


admin.site.register(Games, ListGames)


