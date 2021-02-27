from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path('', views.ArticleList.as_view(), name="article_list")
    path('<int:id>/<slug:slug>/', views.ArticleList.as_view(), name="article_list")
]
