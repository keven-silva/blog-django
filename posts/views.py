from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from posts.models import Post
from comments.models import Comment
from comments.forms import FormComment
from django.db.models import Q, Count, Case, When
from django.contrib import messages
from django.db import connection


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('category_post')
        qs = qs.order_by('-id').filter(publicated_post=True)
        qs = qs.annotate(
            comment_numbers=Count(
                Case(
                    When(comment__comment_publicated=True, then=1)
                )
            )
        )

        return qs

    def get_context_data(self, **kwargs):
        """listening database connections

        Returns:
            _type_: _description_
        """
        contexto = super().get_context_data(**kwargs)
        contexto['connection'] = connection

        return contexto


class PostSearch(PostIndex):
    template_name = 'posts/post_search.html'

    def get_queryset(self):
        qs = super().get_queryset()

        termo = self.request.GET.get('termo', None)

        if not termo:
            return qs

        qs = qs.filter(
            Q(title_post__icontains=termo) |
            Q(author_post__first_name__iexact=termo) |
            Q(content_post__icontains=termo) |
            Q(excerto_post__icontains=termo) |
            Q(category_post__name_cat__icontains=termo)
        )

        return qs


class PostCategory(PostIndex):
    template_name = 'posts/post_category.html'

    def get_queryset(self):
        qs = super().get_queryset()

        category = self.kwargs.get('category', None)

        if not category:
            return qs

        qs = qs.filter(category_post__name_cat__iexact=category)

        return qs


class PostDetail(UpdateView):
    template_name = 'posts/post_detail.html'
    model = Post
    form_class = FormComment
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()
        comment = Comment.objects.filter(
            comment_publicated=True,
            post_comment=post.id)

        contexto['comments'] = comment

        return contexto

    def form_valid(self, form):
        post = self.get_object()
        comment = Comment(**form.cleaned_data)
        comment.post_comment = post

        if self.request.user.is_authenticated:
            comment.comment_user = self.request.user

        comment.save()
        messages.success(self.request, "Comentário enviado com sucesso.")

        return redirect('post_detail', pk=post.id)
