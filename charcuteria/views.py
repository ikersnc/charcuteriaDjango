from django.shortcuts import render
from .models import *

def index(request):
    salazones = Salazones()
    return render(request, 'index.html', {'salazones' : salazones})

def productos(request):
    salazones = Salazones()
    return render(request, 'productos.html', {'salazones' : salazones})