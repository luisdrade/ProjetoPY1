from rest_framework import viewsets
from .models import Orcamentos
from .serializers import orcamentosSerializer

class OrcamentosViewSet(viewsets.ModelViewSet):
    queryset = Orcamentos.objects.all()
    serializer_class = orcamentosSerializer 

# Create your views here.
