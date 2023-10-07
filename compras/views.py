from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CompraSerializer,DetalleCompraSerializer
from .models import Compra,DetalleCompra
# Create your views here.

class CompraView(viewsets.ModelViewSet):
    serializer_class = CompraSerializer
    queryset = Compra.objects.all()

class DetalleCompraView(viewsets.ModelViewSet):
    serializer_class = DetalleCompraSerializer
    queryset = DetalleCompra.objects.all()