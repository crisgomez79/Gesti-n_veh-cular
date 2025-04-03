from django.urls import path
from .views import registrar_vehiculo, success, index

urlpatterns = [
    path('', index, name='index'),  # Route for the home page
    path('registrar/', registrar_vehiculo, name='registrar_vehiculo'),  # Route for vehicle registration
    path('success/', success, name='success'),  # Route for success page
]
