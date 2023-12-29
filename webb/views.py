from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.
 
def home(request):
     data = Game.objects.all()
     return render(request,'index.html',{'data':data})
     
     
def detail(request, **kwargs):
     print(kwargs['id'])
     game = Game.objects.filter(nama=kwargs["id"])
     nominals = Menu.objects.filter(game_name=kwargs["id"])
     
     print(nominals)
     
     if game:
          context = {
               "name" : str(game[0]),
               "image" : game[0].image,
               "nominals" : nominals
          }
          
          return render(request,'detail.html', context)
     

def joki(request, **kwargs):
     game = Joki.objects.all()

     if game:
          context = {
               "data" : game
          }

     return render(request,'joki.html', context)
     
