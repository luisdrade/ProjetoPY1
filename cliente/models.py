from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    empresa = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.nome

# Create your models here.
