from django.db import models
from django.urls import reverse


# Create your models here.
class Ad(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Описание')
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Добавить главное фото')
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Добавить дополнительное фото')
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Добавить дополнительное фото')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'ad_slug': self.slug})

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['pk']
