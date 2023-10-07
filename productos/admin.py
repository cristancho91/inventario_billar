from django.contrib import admin
from .models import CategoriaPro,Subcategoria, Producto, PrecioPorUnidad, UnidadDeMedida,UnidadDeCantidad
# Register your models here.

class CategoriaProAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields=(['nombre'],)
    readonly_fields = ('created','updated')
    list_filter=(['id','nombre'])

class SubCategoriaProAdmin(admin.ModelAdmin):
    list_display = ('nombre','categoria_padre')
    search_fields=(['nombre','categoria_padre'],)
    readonly_fields = ('created','updated')
    list_filter=(['nombre','categoria_padre'])

class ProductAdmin(admin.ModelAdmin):
    list_display=('codigo','nombre','categoria','imagen','stock','disponibilidad','created','updated')
    search_fields=(['codigo','nombre','categoria','disponibilidad'])
    readonly_fields = ('codigo','created','updated')
    list_filter=(['codigo','nombre','categoria'])

class precioUnidadAdmin(admin.ModelAdmin):
    # list_display=['producto']
    list_display=('producto','unidad_de_medida','precio')
    list_filter=(['unidad_de_medida','producto','precio'])
    readonly_fields = ('created','updated')
    search_fields=(['unidad_de_medida','producto','precio'])


class unidadmedidaAdmin(admin.ModelAdmin):
    list_display=('nombre',)
    list_filter=(['nombre'])
    search_fields=(['nombre'])
    readonly_fields = ('created','updated')
    
class unidadCantidadAdmin(admin.ModelAdmin):
    list_display=('nombre',)
    list_filter=(['nombre'])
    search_fields=(['nombre'])
    readonly_fields = ('created','updated')
    

admin.site.register(CategoriaPro, CategoriaProAdmin)
admin.site.register(Subcategoria,SubCategoriaProAdmin )
admin.site.register(Producto,ProductAdmin)
admin.site.register(PrecioPorUnidad,precioUnidadAdmin)
admin.site.register(UnidadDeMedida,unidadmedidaAdmin)
admin.site.register(UnidadDeCantidad, unidadCantidadAdmin)
