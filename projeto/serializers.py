from rest_framework import serializers
from .models import Projeto
from .models import Designer
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome']

class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = ['id', 'nome']
class projetoSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    designers = serializers.PrimaryKeyRelatedField(queryset=Designer.objects.all(), many=True)
    class Meta:
        model = Projeto
        fields = ['id', 'titulo', 'descricao', 'cliente', 'designers', 'data_conclusao']
        
    def validate(self, data):
        if data['data_conclusao'] is None:
            raise serializers.ValidationError("O projeto necessita uma data de conclusão")
        return data