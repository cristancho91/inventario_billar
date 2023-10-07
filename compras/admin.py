from django.contrib import admin
from .models import Compra, DetalleCompra
# Register your models here.

class CompraAdmin(admin.ModelAdmin):
    # list_display = ('proveedor','display_productos','created','updated')
    list_display = ('proveedor','created','updated')
    list_filter =(['proveedor'])
    search_fields = (['proveedor'])
    readonly_fields =('created','updated')
    
    
    # def display_productos(self, obj):
    #     # Este es un método personalizado para mostrar las categorías de un producto
    #     return ", ".join([producto.nombre for producto in obj.producto.all()])
    
    # display_productos.short_description = 'Productos'  # Nombre de la columna en la lista

    
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display =('compra','producto', 'precio_unitario_compra','cantidad','total','created','updated')
    list_filter=(['compra','producto', 'precio_unitario_compra','cantidad','created','updated'])
    search_fields=(['compra','producto', 'precio_unitario_compra'])
    readonly_fields = (['total','created','updated'])
  
    
admin.site.register(Compra, CompraAdmin)
admin.site.register(DetalleCompra, DetalleCompraAdmin)