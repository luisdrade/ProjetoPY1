from django.db import models
from projeto.models import Projeto
from servicos.models import Servicos

class Orcamentos(models.Model):
    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE, related_name='orcamento')
    servicos = models.ManyToManyField(Servicos, related_name='orcamentos')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    aprovado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Orçamento de {self.projeto.titulo}'
# Create your models here.
