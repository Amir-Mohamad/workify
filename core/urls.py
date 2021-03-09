from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = "core"

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('team/about-us/', views.AboutUsList.as_view(), name="about_us"),
    path('contact-us/', views.ContactUs.as_view(), name="contact_us"),
    # path('contact-us/', views.ContactUs.as_view(), name="contact_us"), # CBV
    path('team/work-sample/', TemplateView.as_view(template_name="core/work-sample.html"), name="work_sample"),
]
