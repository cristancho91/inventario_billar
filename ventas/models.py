from django.db import models
from productos.models import Producto
from clientes.models import Clientes
# Create your models here.


class TipoPago(models.Model):
    nombre = models.CharField( max_length=30)
   
    class Meta:
        verbose_name = "tipopago"
        verbose_name_plural = "tipopagos"
        
    def __str__(self):
        return self.nombre
    
class Ventas(models.Model):
    codigo = models.CharField(max_length=100)
    # producto = models.ManyToManyField(Producto, through="DetalleVenta", related_name='detalle_venta')
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True, blank=True)
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        
        # Verifica si es una instancia nueva (no tiene un ID) y genera un código único.
        if not self.id:
            last_venta = Ventas.objects.order_by('-id').first()
            if last_venta:
                last_id = last_venta.id
            else:
                last_id = 0
            self.codigo = f'FACT-{str(last_id + 1).zfill(4)}'

        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "venta"
        verbose_name_plural = "ventas"
        
    def __str__(self):
        return f"Venta con codigo {self.codigo} cliente: {self.cliente} tipo_pago: {self.tipo_pago}"
    
class DetalleVenta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name="detalleVenta"
        verbose_name_plural='detalleVentas'
        
    def __str__(self):
        return f"Detalle de Venta {self.venta.cliente}: {self.cantidad} : {self.producto.nombre}"
        # return self.venta.codigo
    

