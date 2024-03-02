from django.db import models

# Create your models here.

class Produtos(models.Model):
    nome_do_produto = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    preco = models.FloatField()
    max_estoque = models.IntegerField()
    min_estoque = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()