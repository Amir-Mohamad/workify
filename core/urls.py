from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = "core"

urlpatterns = [
    path('', TemplateView.as_view(template_name="core/home.html"), name="home"),
    path('team/about-us/', views.AboutUsList.as_view(), name="about_us"),
    path('contact-us/', TemplateView.as_view(template_name="core/contact-us.html"), name="contact_us"),
    path('team/work-sample/', TemplateView.as_view(template_name="core/work-sample.html"), name="work_sample"),
]
