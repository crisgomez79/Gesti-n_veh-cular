from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehiculos.urls')),  # Route root to vehiculos app
]
