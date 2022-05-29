import random
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import Devinette, Chiffre

# Affiche page de demarrage
def demarrage(request):
    context = {}
    return render(request, 'game/home.html', context)

#Entrer le Pseudo
def pseudo(request):
    context = {}
    return render(request, 'game/home.html', context)

def getdevinettemot(request):
    devinette = Devinette.objects.first()
    context = {}
    return render(request, 'game/devinette.html', context)

def getdevinetteChiffre(request):
    chiffre = Chiffre.objects.first()
    context = {}
    return render(request, 'game/chiffre.html', context)