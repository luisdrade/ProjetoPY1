from rest_framework import serializers
from .models import Projeto

class projetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'
        
    def validate(self, data):
        if data['data_conclusao'] is None:
            raise serializers.ValidationError("O projeto necessita uma data de conclusão")
        return data