from django.db import models

# Create your models here.
class ServicesMoldel(models.Model):

    name = models.CharField(max_length=100)
    descripcion = models.TextField()
    logo = models.CharField(max_length=150)