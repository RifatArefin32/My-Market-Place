from django.contrib import admin
from django.urls import path
from core.views import index, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]

# Serve media files only during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
