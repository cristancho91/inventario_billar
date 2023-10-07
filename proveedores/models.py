from django.db import models

# Create your models here.

class Proveedores(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    nombre_contacto = models.CharField(max_length=100,blank=True,null=True)
    nit = models.CharField(max_length=20, unique=True)
    direccion= models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='proveedores/img', null=True, blank=True, default="prov-defualt.png")
    email = models.EmailField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"
    
    def __str__(self) -> str:
        return self.nombre_empresa
    
# class ProductoProveedor(models.Model):
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now_add=True)
#     # Agrega otros campos relacionados con la relación producto-proveedor, como precio unitario, cantidad, etc.

#     def __str__(self):
#         return f"Producto: {str(self.producto.nombre)}, Proveedor: {str(self.proveedor.nombre_empresa)}"