from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = "core"
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('team/about-us/', views.AboutUsList.as_view(), name="about_us"),
    path('contact-us/', views.ContactUs.as_view(), name="contact_us"),
    # path('contact-us/', views.ContactUs.as_view(), name="contact_us"), # CBV
    path('team/portfolio/', views.Portfolio.as_view(), name="portfolio"),
    path('order/', views.OrderView.as_view(), name="order"),
    path('team/services/', views.ServicesView.as_view(), name="services"),
]
