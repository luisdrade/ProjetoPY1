from django.db import models

class Servicos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco_base = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.nome
# Create your models here.
