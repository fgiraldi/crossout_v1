from django.db import models
from .pieza import Pieza

class Piezas_Storage(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return "%s, %s [%s]" % (self.usuario, self.pieza, self.quantity)