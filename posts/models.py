from django.db import models
from category.models import Category
from django.contrib.auth.models import User


class Post(models.Model):
    title_post = models.CharField(max_length=255, verbose_name='Title')
    author_post = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Author')
    publication_date = models.DateTimeField(
        auto_created=True, auto_now=True, verbose_name='Date')
    content_post = models.TextField(verbose_name='Content')
    excerto_post = models.TextField(verbose_name='Excerto')
    category_post = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Category')
    image_post = models.ImageField(
        upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Image')
    publicated_post = models.BooleanField(
        default=False, verbose_name='Publicated')

    def __str__(self) -> str:
        return self.title_post
