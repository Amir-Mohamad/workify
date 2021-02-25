from django.shortcuts import render
from django.views.generic.edit import FormView

class AboutUs(FormView):
    template_name = 'core/about-us.html'