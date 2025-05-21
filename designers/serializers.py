from rest_framework import serializers
from .models import Designer

class designerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = ['id', 'name', 'especialidade', 'email']
        
    def validade_especialidade(self, value):
        if not value:
            raise serializers.ValidationError("Especialidade é obrigatória")
        return value