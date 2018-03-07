from django.db import models
from .rarity import Rarity

class Pieza(models.Model):
    nombre = models.CharField(max_length=200)
    power_score = models.IntegerField(default=0)
    durability = models.IntegerField(default=0)
    mass = models.IntegerField(default=0)
    crafteable = models.BooleanField(default=True)
    imagen = models.ImageField(null=True, upload_to='uploads/piezas_imagenes')
    rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def es_crafteable(self):
        return self.crafteable