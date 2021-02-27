from django.shortcuts import render
from django.views.generic.list import ListView


class ArticleList(ListView):
    template_name = 'blog/article_list'