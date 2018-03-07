from django.contrib import admin

# Register your models here.
from .models import Rarity, Pieza, Recurso, Piezas_Storage

admin.site.register(Rarity)
admin.site.register(Pieza)
admin.site.register(Recurso)
admin.site.register(Piezas_Storage)
