from django.db import models

class Designer(models.Model):
    ESPECIALIDADES = [
        ('designer', 'Designer Gráfico'),
        ('social_media', 'Social Media'),
        ('videomaker', 'Videomaker'),
    ]
    
    name = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=50, choices=ESPECIALIDADES)
    email = models.EmailField(unique=True)  
    
    def __str__(self):
        return self.name
# Create your models here.
