from django.contrib import admin

from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_name', 'comment_email',
                    'post_comment', 'comment_date', 'comment_publicated')
    list_editable = ('comment_publicated',)
    list_display_link = ('id', 'comment_name', 'comment_email',)


admin.site.register(Comment, CommentAdmin)