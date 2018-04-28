from django import template
register = template.Library()

@register.inclusion_tag('game/rarity_in_config.html')
def rarity_en_config(rarity):
    return {'rarity': rarity}