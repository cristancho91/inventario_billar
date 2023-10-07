from django.contrib import admin
from .models import Ventas, DetalleVenta,TipoPago
# Register your models here.

class VentasAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'cliente', 'tipo_pago','created')
    search_fields=(['codigo', 'cliente', 'tipo_pago','created'])
    readonly_fields=('codigo','created','updated')
    list_filter = (['codigo', 'cliente', 'tipo_pago','created'])

class DetalleVentasAdmin(admin.ModelAdmin):
    list_display = ('producto','venta','cantidad', 'total')
    search_fields=(['producto','venta','created'])
    readonly_fields=('created','updated')
    list_filter = (['producto','venta','cantidad', 'total','created'])


    
admin.site.register(Ventas, VentasAdmin)
admin.site.register(DetalleVenta, DetalleVentasAdmin)
admin.site.register(TipoPago)
