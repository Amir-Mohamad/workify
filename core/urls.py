from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "accounts"
urlpatterns = [
    path('', TemplateView.as_view(template_name="core/home.html"), name="home"),
]
