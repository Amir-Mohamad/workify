from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('', include('core.urls', namespace="core")),
    path('blog/', include('blog.urls', namespace="blog")),
    path('admin/', admin.site.urls),
]
handler404 = 'core.views.handler404'

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
