from rest_framework import viewsets
from .models import Projeto
from .serializers import projetoSerializer

class projetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = projetoSerializer


# Create your views here.
