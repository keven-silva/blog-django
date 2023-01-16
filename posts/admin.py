from django.contrib import admin
from posts.models import Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title_post', 'author_post',
                    'publication_date', 'category_post', 'publicated_post')
    list_editable = ('publicated_post',)
    list_display_links = ('id', 'title_post',)
    summernote_fields = ('content_post',)


admin.site.register(Post, PostAdmin)