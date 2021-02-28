from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path('', views.ArticleList.as_view(), name="article_list"),
    path('<int:id>/<slug:slug>/', views.ArticleDetail.as_view(), name="article_detail"),
    path('<str:category>/', views.CategoryList.as_view(), name="article_by_category"),
]
