from django.urls import include, path
from rest_framework import routers
from .views import ClientesView
router = routers.DefaultRouter()
router.register(r'clientes', ClientesView,'clientes')
urlpatterns = [
    path('',include(router.urls), name='clientes'),
]