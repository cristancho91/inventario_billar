from django.contrib import admin
from .models import Clientes
# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email','telefono','direccion')
    list_filter=(['nombre', 'email','telefono','direccion'])
    search_fields=(['nombre', 'email','telefono','direccion'])
    readonly_fields =('created','updated')

admin.site.register(Clientes,ClienteAdmin)
