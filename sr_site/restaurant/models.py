from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ten menu')  # Text
    description = models.TextField(blank=True, verbose_name='description')  # Description / Не обязательное
    price = models.IntegerField(verbose_name='Gia')  # Price
    photo = models.ImageField(blank=True, upload_to='photos/%y/%m/%d', verbose_name='photo')  # Photo
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Ngay doi')
    is_published = models.BooleanField(default=True, verbose_name='Hien/Dau')  # Default = none

    def __str__(self):
        return self.name

    # Для админки
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'All menu'
        # ordering = ['-created_at', 'price']
        ordering = ['-price']    # Влияет на админку и на сайт






