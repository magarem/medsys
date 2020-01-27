from django.db import models

class Remedio(models.Model):
    codigo = models.CharField(max_length=20, blank=True, null=True)
    nome = models.CharField(max_length=200)
    unidade = models.CharField(max_length=10, default='uni')
    validade = models.DateField('validade', blank=True, null=True)
    obs = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome

    
