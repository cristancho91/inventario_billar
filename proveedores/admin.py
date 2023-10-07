from django.contrib import admin
from .models import Proveedores
# Register your models here.

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('nombre_empresa','nombre_contacto', 'nit','direccion','telefono','imagen','email')
    readonly_fields = ('created','updated')
    search_fields = (['nombre_empresa','nombre_contacto', 'nit','direccion','telefono','imagen','email'])
    list_filter = (['nombre_empresa','nombre_contacto', 'nit','direccion','telefono'])




admin.site.register(Proveedores, ProveedoresAdmin)