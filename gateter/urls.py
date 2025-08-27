from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meows.urls')),   # incluye las rutas de la app meows
]
