
from django.db import models

class Vehiculo(models.Model):
    numero_unico = models.CharField(max_length=50, unique=True)
    patente = models.CharField(max_length=50)
    numero_chasis = models.CharField(max_length=50)
    numero_motor = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    autopartes = models.TextField()
    qr_code = models.ImageField(upload_to="qr_codes/", null=True, blank=True)

    def __str__(self):
        return f"{self.patente} - {self.numero_unico}"

class VehiculoFoto(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, related_name="fotos", on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="imagenes_vehiculos/")

    def __str__(self):
        return f"Foto de {self.vehiculo.patente}"
