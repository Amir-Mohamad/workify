from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from .models import Article, Category
from django.views.generic.detail import DetailView


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
    template_name = 'blog/category_list.html'
