
from django.contrib import admin
from django.urls import path
from webb.views import home,menu
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('menu/', menu),
]
