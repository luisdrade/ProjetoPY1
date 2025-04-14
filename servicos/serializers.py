from rest_framework import serializers
from .models import Servicos

class servicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = '__all__'

    def validate_preco_base(self, value):
        if value < 50:
            raise serializers.ValidationError("O preço não pode ser menor que 50 reais")
        return value