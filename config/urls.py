"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('accounts.urls', namespace="accounts")),
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 93a180c86b0f9e526d58cde7058532e7682a8f61
=======
>>>>>>> ali
>>>>>>> 3adfdb2b59297ec129c99c0dc7150e1e4997db7b
=======
>>>>>>> 6fa5f51ee28cbad4f2a2443e56b95aefb0712f69
    path('', include('core.urls', namespace="core")),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    # urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)