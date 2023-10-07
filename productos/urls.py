from django.urls import include, path
from rest_framework import routers
from .views import ProductoView,PrecioPorUnidadView,CategoriaProView,SubcategoriaView,UnidadDeCantidadView,UnidadDeMedidaView
router = routers.DefaultRouter()
router.register(r'productos', ProductoView,'productos')
router.register(r'categoriaPoducto', CategoriaProView,'categoriaPoducto')
router.register(r'precio-unidad', PrecioPorUnidadView,'precio-unidad')
router.register(r'subcategoria-producto', SubcategoriaView,'subcategoria-producto')
router.register(r'unidad-cantidad', UnidadDeCantidadView,'unidad-cantidad')
router.register(r'unidad-medida', UnidadDeMedidaView,'unidad-medida')
urlpatterns = [
    path('',include(router.urls), name='productos'),
    path('',include(router.urls), name='categoriaPoducto'),
    path('',include(router.urls), name='precio-unidad'),
    path('',include(router.urls), name='subcategoria-producto'),
    path('',include(router.urls), name='unidad-cantidad'),
    path('',include(router.urls), name='unidad-medida'),
]