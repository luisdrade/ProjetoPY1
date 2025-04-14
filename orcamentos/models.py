from django.db import models
from projeto.models import Projeto
from servicos.models import Servicos

class Orcamentos(models.Model):
    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servicos)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return f'Orçamento de {self.projeto.titulo}'
# Create your models here.
