from rest_framework import serializers
from .models import Cliente

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def validate_nome(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("O nome deve ter no mínimo 3 caracteres")
        return value