from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ClientesSerializer
from .models import Clientes
# Create your views here.

class ClientesView(viewsets.ModelViewSet):
    serializer_class = ClientesSerializer
    queryset = Clientes.objects.all()