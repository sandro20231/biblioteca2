from django.db import models

# Create your models here.


class Autor(models.Model):
    nome = models.CharField(max_length=64)
    idade = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.idade}"


class Livro(models.Model):
    titulo = models.CharField(max_length=64)
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, related_name="objetoautor")
    resumo = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.resumo}"
