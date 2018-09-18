from django.db import models


class Endereco(models.Model):
    '''
    Usando os atributos linha1 e linha2, irá deixar a modelagem
    generica, uma vez que nem todos os pontos turisticos estão em rua, bairro..
    '''

    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=60)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1
