from django.db import models

# Create your models here.

class Pessoa(models.Model):
    name = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    
class Marca(models.Model):
    name = models.CharField(max_length=50)
    
    
class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()