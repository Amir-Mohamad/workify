from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Article, Category



class ArticleList(ListView):
    template_name = 'blog/article_list.html'

