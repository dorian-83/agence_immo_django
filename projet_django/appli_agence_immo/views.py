from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from . import models

# Create your views here.


def main(request):
    return render(request, 'main.html')



def ajouter_acheteur(request):
    if request.method == 'POST':
        form = AcheteursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')  # redirige vers une autre vue ou page
    else:
        form = AcheteursForm()
    return render(request, 'ajouter_acheteur.html', {'form': form})

def ajouter_vendeur(request):
    if request.method == 'POST':
        form = VendeursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')  # redirige vers une autre vue ou page
    else:
        form = VendeursForm()
    return render(request, 'ajouter_vendeur.html', {'form': form})
