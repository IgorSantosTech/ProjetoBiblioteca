from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    anoPub = models.IntegerField()