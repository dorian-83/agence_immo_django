from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AcheteursForm
from . import models

# Create your views here.


def main(request):
    return HttpResponse("<h1>page d'accueil</h1>")

def ajouter_acheteur(request):
    if request.method == 'POST':
        form = AcheteursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')  # redirige vers une autre vue ou page
    else:
        form = AcheteursForm()
    return render(request, 'ajouter_client.html', {'form': form})
