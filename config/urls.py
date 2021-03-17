from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('learn/', include('learn.urls', namespace="learn")),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    # path('blog/', include('blog.urls', namespace="blog")),
    path('', include('core.urls', namespace="core")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)