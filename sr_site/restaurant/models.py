from django.db import models
from django.urls import reverse  # or reverse_lazy


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ten menu')  # Text
    description = models.TextField(blank=True, verbose_name='description')  # Description / Не обязательное
    price = models.IntegerField(verbose_name='Gia')  # Price
    photo = models.ImageField(blank=True, upload_to='photos/%y/%m/%d', verbose_name='photo')  # Photo
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Ngay doi')
    is_published = models.BooleanField(default=True, verbose_name='Hien/Dau')  # Default = none
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Loai menu')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_menu', kwargs={'pk': self.pk})

    # Для админки
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'All menu'
        # ordering = ['-created_at', 'price']
        ordering = ['-price']    # Влияет на админку и на сайт


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Ten menu')  # Index field in Admin panel
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Ngay doi')

    def __str__(self):  # {{ item.category }} Иначе {{ item.category.title }}
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Loai menu'
        verbose_name_plural = 'All loai menu'
        ordering = ['-title']  # Sort by -title


class Games(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='game_name')  # Index field
    about_game = models.TextField(blank=True, verbose_name='about_game')  # Description / Не обязательное
    photo = models.ImageField(blank=True, upload_to='photos/%y/%m/%d', verbose_name='game image')  # Photo
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Ngay doi')

    def __str__(self):  # {{ item.category }} Иначе {{ item.category.title }}
        return self.name

    def get_absolute_url(self):
        return reverse('game', kwargs={'game_id': self.pk})

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        ordering = ['name']  # Sort by -name

