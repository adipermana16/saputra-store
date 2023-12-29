from django.contrib import admin
from django.urls import include, path

urlpatterns = [
        path('', include('webb.urls')),
        path('admin/', admin.site.urls),
        path('joki.html', Joki.site.urls)
    ]