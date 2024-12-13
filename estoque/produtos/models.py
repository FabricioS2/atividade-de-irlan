from django.db import models

# Create your models here.

class Produto(models.Model):
    Nome = models.CharField("Nome do produto",max_length=200,blank=False, null=False)
    Codigo_do_produto = models.CharField("Código do produto",max_length=200, unique=True, blank=False, null=False)
    Descricao = models.CharField("Descrição",max_length=900,blank=True)
    Preco = models.DecimalField("Preço",max_digits=10, decimal_places=2)
    Quantidade_em_estoque = models.DecimalField("Quantidade em estoque",decimal_places=0,max_digits=5)
    Data_de_criacao = models.DateField("Data de criação", auto_now_add=True)
