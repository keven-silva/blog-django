from django.db import models
from django.contrib.auth.models import User

from posts.models import Post


class Comment(models.Model):
    comment_name = models.CharField(max_length=50, verbose_name='Nome')
    comment_email = models.EmailField(max_length=254, verbose_name='Email')
    comment = models.TextField(max_length=255, verbose_name='Comentário')
    post_comment = models.ForeignKey(
        Post,  on_delete=models.CASCADE, verbose_name='Post')
    comment_user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='User')
    comment_date = models.DateTimeField(
        auto_created=True, auto_now=True, verbose_name='Date')
    comment_publicated = models.BooleanField(default=False, verbose_name='Publicated')

    def __str__(self) -> str:
        return self.comment_name
