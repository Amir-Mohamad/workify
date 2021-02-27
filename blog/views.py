from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Article, Category
from django.views.generic.detail import DetailView


class ArticleList(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.filter(is_active=True)

class ArticleDetail(DetailView):
    model = Article