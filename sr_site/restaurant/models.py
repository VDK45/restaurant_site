from django.db import models
from django.urls import reverse  # or reverse_lazy
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ten menu')  # Text
    description = models.TextField(blank=True, verbose_name='description')  # Description / Не обязательное
    # description = RichTextField(blank=True, verbose_name='description')  # Description / Не обязательное
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
        verbose_name = 'Thực đơn'
        verbose_name_plural = 'Tất cả thực đơn'
        # ordering = ['-created_at', 'price']
        ordering = ['-price']    # Влияет на админку и на сайт


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Ten menu')  # Index field in Admin panel
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Ngay doi')

    # Для ORM тоже
    def __str__(self):  # {{ item.category }} Иначе {{ item.category.title }}
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Loại đồ ăn'
        verbose_name_plural = 'Tât cả các loại đồ ăn'
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


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, help_text='Không quuá 250 ký tự', verbose_name='Đề tài')
    content = models.TextField(max_length=2000, blank=True, help_text='Không quuá 2000 ký tự', null=True,
                               verbose_name='van ban')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Ngày gi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Ngày đổi')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Bình luan'
        verbose_name_plural = 'Tat ca Bình luan'


# class StatusCommentFilter(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status=False)


class Comments(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Đồ ăn', blank=True, null=True,
                             related_name='comments_menu')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Người viết', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Ngày tạo ra')
    text = models.TextField(max_length=2000, blank=True, null=True,
                            verbose_name='Góp ý', help_text='<li>Xin quý vị đừng viết bậy!</li>'
                                                              '<li>Không quá 2000 ký tự.</li>')
    status = models.BooleanField(verbose_name='Hiện/dấu', default=False)
    # objects = StatusCommentFilter()

    class Meta:
        verbose_name = 'Góp ý'
        verbose_name_plural = 'Góp ý'
        ordering = ['status']
