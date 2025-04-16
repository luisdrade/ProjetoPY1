from django.db import models


class Servicos(models.Model):
    TIPOS_SERVICO = [
        ('video', 'Edição de Vídeo'),
        ('social_media', 'Social Media'),
        ('design', 'Designer Gráfico'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPOS_SERVICO, default='design')
    descricao = models.TextField()
    preco_base = models.DecimalField(max_digits=8, decimal_places=2,verbose_name="Preço Base (R$)")
    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()}"
# Create your models here.
