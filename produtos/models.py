from django.db import models


class Product(models.Model):
    TYPE_CHOICES = (
        ('A', 'audio'),
        ('V', 'video'),
        ('AV', 'audio/video'),
        ('F', 'foto'),
        ('CEL', 'celular'),
        ('NB', 'notebook'),
        ('O', 'outros'),
    )
    STATUS_CHOICES = (
        ('D', 'disponivel'),
        ('I', 'indisponivel')
    )
    nome = models.CharField(max_length=50)
    descricao = models.TextField(name='Descrição', max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=3, choices=TYPE_CHOICES, blank=False, default='')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, default='')
    obs_status = models.CharField(max_length=100, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    especificacao = models.TextField(name='Especificação', blank=True, null=True)
    foto = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.nome
