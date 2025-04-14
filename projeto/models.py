from django.db import models
from cliente.models import Cliente
from designers.models import Designer

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    designer = models.ManyToManyField(Designer)
    data_conclusao = models.DateField()
    
    def __str__(self):
        return self.titulo