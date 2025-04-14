from rest_framework import viewsets
from .models import Servicos
from .serializers import servicoSerializer

class ServicosViewSet(viewsets.ModelViewSet):
    queryset = Servicos.objects.all()
    serializer_class = servicoSerializer
    
# Create your views here.
