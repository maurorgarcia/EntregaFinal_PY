from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("accounts/", include("accounts.urls")),
    path("messages/", include("messenger.urls")),
]

if settings.DEBUG:
    # En desarrollo, servir uploads desde MEDIA_URL (avatar, imágenes de pages).
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
