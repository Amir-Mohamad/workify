from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
	path('login/', views.UserLogin.as_view(), name='login'),
	path('logout/', views.UserLogout, name='logout'),
	path('register/', views.UserRegister.as_view(), name='register'),
]