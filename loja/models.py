from django.db import models
from django.conf import settings


class Marca(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Peca(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ManyToManyField(Marca, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    codigo = models.CharField(max_length=20)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    imagem = models.ImageField(upload_to='loja/media', blank=True)
    ano = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome
