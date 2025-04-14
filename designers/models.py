from django.db import models

class Designer(models.Model):
    name = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  
    
    def __str__(self):
        return self.name
# Create your models here.
