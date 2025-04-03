
from django import forms
from .models import Vehiculo, VehiculoFoto

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'numero_chasis', 'numero_motor', 'color', 'marca', 'modelo', 'autopartes']

VehiculoFotoFormSet = forms.inlineformset_factory(
    Vehiculo, VehiculoFoto, fields=['foto'], extra=3, can_delete=True
)
