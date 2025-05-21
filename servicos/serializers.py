from rest_framework import serializers
from .models import Servicos

class servicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = ['id', 'nome', 'tipo','descricao', 'preco_base']

    def validate_preco_base(self, value):
        if value < 50:
            raise serializers.ValidationError("O preço não pode ser menor que 50 reais")
        return value