from rest_framework import serializers
from .models import Orcamentos

class orcamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orcamentos
        fields = '__all__'
        
    def validade_valor_total(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor total tem que ser maior que zero")
        return value