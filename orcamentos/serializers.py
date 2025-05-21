from rest_framework import serializers
from .models import Orcamentos

class orcamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orcamentos
        fields = ['projeto', 'servicos', 'valor_total', 'aprovado', 'criado_em']
        
    def validade_valor_total(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor total tem que ser maior que zero")
        return value