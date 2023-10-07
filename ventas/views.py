from django.shortcuts import render
from rest_framework import viewsets
from .serializer import DetalleVentaSerializer,VentasSerializer,TipoPagoSerializer
from .models import Ventas,DetalleVenta,TipoPago
# Create your views here.

class VentasView(viewsets.ModelViewSet):
    serializer_class = VentasSerializer
    queryset = Ventas.objects.all()

class DetalleVentaView(viewsets.ModelViewSet):
    serializer_class = DetalleVentaSerializer
    queryset = DetalleVenta.objects.all()

class TipoPagoView(viewsets.ModelViewSet):
    serializer_class = TipoPagoSerializer
    queryset = TipoPago.objects.all()