from django.shortcuts import render

def index(request):
    return render(request, 'vehiculos/index.html')

def registrar_vehiculo(request):
    # Placeholder logic for vehicle registration
    return render(request, 'vehiculos/registrar.html')

def success(request):
    return render(request, 'vehiculos/success.html')
