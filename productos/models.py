from django.db import models
# Create your models here.
class CategoriaPro(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="categoriaPro"
        verbose_name_plural='categoriaProds'
    
    def __str__(self) -> str:
        return self.nombre

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=100)
    categoria_padre = models.ForeignKey(CategoriaPro, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria_padre} - {self.nombre}"
    
class Producto(models.Model):
    codigo = models.CharField(max_length=10, unique=True, editable=False)
    # descripcion = models.TextField('Descripcion', max_length=1024, blank=False,)
    nombre = models.CharField( max_length=100 )
    categoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/img',blank=True, null=True)
    stock = models.IntegerField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
     # restricción de verificación para asegurarse de que el precio y la cantidad sean valores positivos.
    # check_precio_positivo = models.CheckConstraint(
    #     check=models.Q(precio_venta_u__gt=0) & models.Q(cantidad__gt=0),
    #     check=models.Q(precio_venta_u__gt=0),
    #     name='precio_venta_positivo'
    # )
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        
    def save(self, *args, **kwargs):
        
        # Verifica si es una instancia nueva (no tiene un ID) y genera un código único.
        if not self.id:
            last_product = Producto.objects.order_by('-id').first()
            if last_product:
                last_id = last_product.id
            else:
                last_id = 0
            self.codigo = f'PR-{str(last_id + 1).zfill(4)}'

        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.nombre
    
class UnidadDeMedida(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "unidadMedida"
        verbose_name_plural = "unidadMedidas"
        
    def __str__(self):
        return self.nombre

class UnidadDeCantidad(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "UnidadDeCantidad"
        verbose_name_plural = "UnidadDeCantidades"
        
    def __str__(self):
        return self.nombre
    
class PrecioPorUnidad(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    unidad_de_medida = models.ForeignKey(UnidadDeMedida, on_delete=models.CASCADE)
    unidad_de_cantidad = models.ForeignKey(UnidadDeCantidad, on_delete=models.CASCADE)
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "PrecioPorUnidad"
        verbose_name_plural = "PrecioPorUnidades"
    
    def __str__(self):
        return f"{str(self.producto)} - {str(self.unidad_de_medida)}: {str(self.precio)}" 
    