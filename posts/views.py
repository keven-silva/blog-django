from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic.list import ListView
from django.views import View
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


class PostDetail(View):
    template_name = 'posts/post_detail.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk, publicated_post=True)

        self.contexto = {
            'post': post,
            'comments': Comment.objects.filter(post_comment=post,
                                               comment_publicated=True),
            'form': FormComment(request.POST or None)
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = self.contexto['form']

        if not form.is_valid():
            return render(request, self.template_name, self.contexto)

        comment = form.save(commit=False)

        if request.user.is_authenticated:
            comment.comment_user = request.user

        comment.post_comment = self.contexto['post']
        comment.save()
        messages.success(request, 'Seu comentário está em revisão.')

        return redirect('post_detail', pk=self.kwargs.get('pk'))