from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import clienteViewSet

router = DefaultRouter()
router.register(r'', clienteViewSet) #aqui se registra o endpoint de clientes e o viewset que será utilizado

urlpatterns = [
    path('', include(router.urls)),
]