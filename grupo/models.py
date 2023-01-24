from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    codinome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'Pessoa [nome={self.nome}]'

