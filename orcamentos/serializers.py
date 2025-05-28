from rest_framework import serializers
from .models import Orcamentos
from projeto.models import Projeto
from servicos.models import Servicos

class orcamentosSerializer(serializers.ModelSerializer):
    nome_projeto = serializers.SerializerMethodField()
    nomes_servicos = serializers.SerializerMethodField()
    
    class Meta:
        model = Orcamentos
        fields = ['id','projeto', 'nome_projeto', 'nomes_servicos', 'servicos', 'valor_total', 'aprovado', 'criado_em']
        
    def get_nome_projeto(self, obj):
        return obj.projeto.titulo  

    def get_nomes_servicos(self, obj):
        return [servico.nome for servico in obj.servicos.all()]
        
    def validade_valor_total(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor total tem que ser maior que zero")
        return value
    def validate_projeto(self, value):
        if Orcamentos.objects.filter(projeto=value).exists():
            raise serializers.ValidationError("Já existe um orçamento cadastrado para esse projeto.")
        return value