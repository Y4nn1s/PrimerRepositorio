from django import forms
from .models import Empleado, Atencion

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = '__all__'
