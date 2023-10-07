from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from proveedores.models import Proveedores 
from productos.models import Producto
# Create your models here.




class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    # producto = models.ManyToManyField(Producto, through="DetalleCompra", related_name='detalle_compra')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="compra"
        verbose_name_plural='compras'

    def __str__(self):
        return f"Compra de {str(self.proveedor.nombre_empresa)}"

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_unitario_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cantidad = models.IntegerField()
    total = models.FloatField( blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def calcular_total(self):
        # Calcula el total multiplicando cantidad y precio_unitario
        return self.cantidad * self.precio_unitario_compra
    
    class Meta:
        verbose_name="detalleCompra"
        verbose_name_plural='detalleCompras'
        
    def __str__(self):
        return f"Detalle de compra {self.compra.id}: {self.cantidad} {self.producto.nombre}"

@receiver(pre_save, sender=DetalleCompra)
def actualizar_total_detalle_compra(sender, instance, **kwargs):
    # Actualiza el campo 'total' antes de guardar la instancia
    instance.total = instance.calcular_total()