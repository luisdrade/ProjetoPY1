from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DesignerViewSet

router = DefaultRouter()
router.register(r'designers', DesignerViewSet) #aqui se registra o endpoint de designers e o viewset que será utilizado

urlpatterns = [
    path('', include(router.urls)),
]