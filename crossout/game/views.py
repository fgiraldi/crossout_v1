from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Piezas_Storage
from .models import Rarity

def index(request):    
    return HttpResponse("Hello Crossout user")

def welcome(request):
    context = {}
    return render(request, 'game/welcome.html', context)

def user_storage(request, user_id):
    piezas_almacenadas = Piezas_Storage.objects.filter(usuario_id=user_id)
    raritys = Rarity.objects.all()
    context = {'user_id': user_id, 'piezas_almacenadas': piezas_almacenadas, 'raritys': raritys}
    return render(request, 'game/user_storage.html', context)