from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = "accounts"

urlpatterns = [
    path('', TemplateView.as_view(template_name="core/home.html"), name="home"),
    path('team/about-us/', TemplateView.as_view(template_name="core/about-us.html"), name="about_us"),
    path('contact-us/', TemplateView.as_view(template_name="core/contact-us.html"), name="contact_us"),
    path('contact-us/', TemplateView.as_view(template_name="core/work-sample.html"), name="work_sample"),
]

# forms => fields => FormView => contact us 