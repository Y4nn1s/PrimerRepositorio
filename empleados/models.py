from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
# Otros campos relevantes para los empleados

class Atencion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    
    fecha = models.DateTimeField(auto_now_add=True)
# Otros campos relevantes para el registro de atención








