from django.shortcuts import render
from django.views.generic.list import ListView


class AboutUsList(ListView):
    template_name = 'core/about-us.html'