from rest_framework import serializers
from .models import Producto,PrecioPorUnidad,CategoriaPro,Subcategoria,UnidadDeCantidad,UnidadDeMedida

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
class PrecioPorUnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecioPorUnidad
        fields = '__all__'

class CategoriaProSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPro
        fields = '__all__'

class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = '__all__'

class UnidadDeCantidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadDeCantidad
        fields = '__all__'
    

class UnidadDeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadDeMedida
        fields = '__all__'