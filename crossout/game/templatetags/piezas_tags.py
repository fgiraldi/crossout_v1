from django import template
register = template.Library()

@register.inclusion_tag('game/pieza_in_storage.html')
def pieza_en_almacen(pieza):
    return {'pieza_almacenada': pieza}