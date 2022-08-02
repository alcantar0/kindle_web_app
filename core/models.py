from django.db import models

class Arquivo(models.Model):
    file = models.FileField(upload_to="files/")

