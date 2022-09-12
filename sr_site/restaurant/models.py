from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')  # Text
    description = models.TextField(blank=True, verbose_name='description')  # Description / Не обязательное
    price = models.IntegerField(verbose_name='price')  # Price
    photo = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='photo')  # Photo
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated')
    is_published = models.BooleanField(default=True, verbose_name='published')  # Default = none

    def __str__(self):
        return self.name







