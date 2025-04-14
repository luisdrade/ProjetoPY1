from rest_framework import viewsets
from .models import Cliente
from .serializers import clienteSerializer

class clienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all() #no queryset faz o select do banco de dados e traz os dados do banco de dados para o serializer no formato json
    serializer_class = clienteSerializer #serializer

# Create your views here.
