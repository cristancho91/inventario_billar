from django.urls import include, path
from rest_framework import routers
from .views import DetalleVentaView,TipoPagoView,VentasView
router = routers.DefaultRouter()
router.register(r'ventas', VentasView,'ventas')
router.register(r'detalle-venta', DetalleVentaView,'detalle-venta')
router.register(r'tipo-pago', TipoPagoView,'tipo-pago')
urlpatterns = [
    path('',include(router.urls), name='ventas'),
    path('',include(router.urls), name='detalle-venta'),
    path('',include(router.urls), name='tipo-pago'),
]