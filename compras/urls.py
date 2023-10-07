from django.urls import include, path
from rest_framework import routers

from .views import CompraView,DetalleCompraView
router = routers.DefaultRouter()

router.register(r'compras', CompraView,'compras')
router.register(r'detalle-compra', DetalleCompraView,'detalle-compra')
urlpatterns = [
    path('',include(router.urls), name='compras'),
    
]