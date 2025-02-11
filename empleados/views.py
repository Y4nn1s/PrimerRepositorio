
#Creación de las vistas de empleados
from django.shortcuts import render, redirect
from .models import Empleado, Atencion
from .forms import EmpleadoForm, AtencionForm

def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
        
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/registrar_empleado.html', {'form': form})
# Vistas para gestionar la atención, lista de empleados, etc.