from django.db import models

# Create your models here.
class UserModel(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=100)