from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "accounts"
urlpatterns = [
    path('', TemplateView.as_view(template_name="core/home.html"), name="home"),
    path('team/about-us/', TemplateView.as_view(template_name="core/aboutus.html"), name="home"),
    path('contact-us/', TemplateView.as_view(template_name="core/contactus.html"), name="home"),
]
