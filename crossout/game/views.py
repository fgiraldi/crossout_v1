from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Piezas_Storage
from .models import Rarity

class ItemMenu:
    """ Los items que se muestran  en el menu """

    def __init__(self, texto, vista):
        self.texto = texto
        self.view = vista
        self.selected = False

    def __str__(self):
        return self.texto

    def select(self):
        self.selected = True
    
    def unselect(self):
        self.selected = False
    
    def unselectAllExceptThis(self, items):
        for i in items:
            i.unselect()
        self.select()

btnGarage = ItemMenu('Garage', 'garage')
btnStorage = ItemMenu('Storage', 'user_storage')
btnMarket = ItemMenu('Market', 'market')
btnLogOut = ItemMenu('Logout', 'logout')
items_menu = [btnGarage, btnMarket, btnStorage, btnLogOut]

def index(request):    
    return HttpResponse("Hello Crossout user")

def welcome(request):
    context = {}
    return render(request, 'game/welcome.html', context)

@login_required
def user_storage(request):
    ItemMenu.unselectAllExceptThis(btnStorage, items_menu)    
    piezas_almacenadas = Piezas_Storage.objects.filter(usuario=request.user)    
    raritys = Rarity.objects.all()
    context = {'user_id': request.user, 'piezas_almacenadas': piezas_almacenadas, 'raritys': raritys, 'items_menu': items_menu}
    return render(request, 'game/user_storage.html', context)

@login_required
def garage(request):
    ItemMenu.unselectAllExceptThis(btnGarage, items_menu)
    context = {'user_id': request.user, 'items_menu': items_menu}
    return render(request, 'game/garage.html', context)

@login_required    
def market(request):
    ItemMenu.unselectAllExceptThis(btnMarket, items_menu)
    context = {'user_id': request.user, 'items_menu': items_menu}
    return render(request, 'game/market.html', context)
   
def logout_view(request):
    logout(request)
    return redirect('loggedout')

def loggedout(request):
    return render(request, 'game/logout.html')