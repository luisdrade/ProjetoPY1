from django.db import models
from cliente.models import Cliente
from designers.models import Designer

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='projetos')
    designers = models.ManyToManyField(Designer, related_name='projetos')
    data_conclusao = models.DateField()

    
    def __str__(self):
        return f"{self.titulo} - {self.cliente.nome}"