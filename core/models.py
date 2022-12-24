"""Modelos para o app core"""
from django.db import models


class Arquivo(models.Model):
    """Modelo para aquivos"""

    file = models.FileField(upload_to="files/")


class Livro(models.Model):
    """Modelo para livros"""

    titulo = models.TextField(max_length=500)
    data = models.TextField()
    highlight = models.TextField()
    anotacao = models.TextField(null=True)
