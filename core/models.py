
from pyexpat import model
from django.db import models

# Create your models here.
class endereco(models.Model):
    cep = models.CharField(
        max_length=7
    )
    cidade_estado = models.CharField(
        max_length=128
    )
    bairro = models.CharField(
        max_length=64
    )
    logradouro = models.CharField(
        max_length=1024
    )
    edificio = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

class Edificio(models.Model):
    enderecinho = models.CharField(
        max_length=256
    )