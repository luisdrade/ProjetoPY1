from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import projetoViewSet

router = DefaultRouter()
router.register(r'', projetoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]