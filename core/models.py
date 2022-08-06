"""Modelos para o app core"""
from django.db import models


class Arquivo(models.Model):
    """Modelo para aquivos"""

    file = models.FileField(upload_to="files/")
