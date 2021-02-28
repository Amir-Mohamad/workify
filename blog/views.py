from django.db.models import query
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from .models import Article, Category
from django.views.generic.detail import DetailView
from accounts.models import User

class ArticleList(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.filter(is_active=True)

class ArticleDetail(DetailView):
    template_name = 'blog/article_detail.html'
    # query_pk_and_slug = True (Im not sure but i think this will do the same get_queryset())
    
    def get_queryset(self):
        id = self.kwargs['id']
        slug = self.kwargs['slug']
        queryset = get_object_or_404(Article, id=id, slug=slug)
        return queryset

class CategoryList(ListView):
    paginate_by = 5
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.is_active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context



class AuthorList(ListView):
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
