from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CategoriaProSerializer,PrecioPorUnidadSerializer,ProductoSerializer,SubcategoriaSerializer,UnidadDeCantidadSerializer,UnidadDeMedidaSerializer
from .models import UnidadDeCantidad,CategoriaPro,PrecioPorUnidad,Producto,Subcategoria,UnidadDeMedida
# Create your views here.

class CategoriaProView(viewsets.ModelViewSet):
    serializer_class = CategoriaProSerializer
    queryset = CategoriaPro.objects.all()

class PrecioPorUnidadView(viewsets.ModelViewSet):
    serializer_class = PrecioPorUnidadSerializer
    queryset = PrecioPorUnidad.objects.all()

class ProductoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    
class SubcategoriaView(viewsets.ModelViewSet):
    serializer_class = SubcategoriaSerializer
    queryset = Subcategoria.objects.all()

class UnidadDeCantidadView(viewsets.ModelViewSet):
    serializer_class = UnidadDeCantidadSerializer
    queryset = UnidadDeCantidad.objects.all()
    
class UnidadDeMedidaView(viewsets.ModelViewSet):
    serializer_class = UnidadDeMedidaSerializer
    queryset = UnidadDeMedida.objects.all()