
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProveedoresSerializer
from .models import Proveedores
# Create your views here.


class ProveedoresView(viewsets.ModelViewSet):
    serializer_class = ProveedoresSerializer
    queryset = Proveedores.objects.all()