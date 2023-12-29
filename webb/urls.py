from django.urls import path
from . import views
from store import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<id>', views.detail, name='details'),
    path('joki/<id>', views.joki, name='joki'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)