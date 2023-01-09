from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from outdoor import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', namespace='about')),
    path('tinymce/', include('tinymce.urls')),
    path('', include('posts.urls', namespace='posts')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = pageNotFound
