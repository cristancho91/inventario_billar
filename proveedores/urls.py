from django.urls import include, path
from rest_framework import routers
from .views import ProveedoresView
router = routers.DefaultRouter()
router.register(r'proveedores', ProveedoresView,'proveedores')
urlpatterns = [
    path('',include(router.urls), name='proveedores'),
]