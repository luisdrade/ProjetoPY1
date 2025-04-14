from rest_framework import viewsets
from .models import Designer
from .serializers import designerSerializer

class DesignerViewSet(viewsets.ModelViewSet):
    queryset = Designer.objects.all()
    serializer_class = designerSerializer

# Create your views here.
