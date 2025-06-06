from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServicosViewSet

router = DefaultRouter()
router.register(r'', ServicosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]