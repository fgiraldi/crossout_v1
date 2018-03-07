from django.db import models

# Create your models here.
class Rarity(models.Model):
    nombre = models.CharField(max_length=200)
    orden = models.IntegerField(default=0)
    color = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.nombre
