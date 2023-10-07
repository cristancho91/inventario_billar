from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField( max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
    
    def __str__(self) -> str:
        return self.nombre    