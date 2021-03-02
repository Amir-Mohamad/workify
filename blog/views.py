from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from accounts.models import User
from .models import Article, Category


class ArticleList(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.filter(is_active=True)
    context_object_name = 'articles'


class ArticleDetail(DetailView):
    context_object_name = 'articles'

    def get_object(self):
            slug = self.kwargs.get('slug')
            id = self.kwargs.get('id')
            article = get_object_or_404(Article, id=id, slug=slug)
            return article


class CategoryList(ListView):
    paginate_by = 5
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.filter(is_active=True), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

# This Will Show the posts owned by a Specified user
class AuthorList(ListView):
    paginate_by = 5
    template_name = 'blog/author_list.html'

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
