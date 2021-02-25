from django.shortcuts import render
from django.views.generic.list import ListView
from .models import AboutUsModel

class AboutUsList(ListView):
    queryset = AboutUsModel.objects.filter(active=True)
    template_name = 'core/about-us.html'
