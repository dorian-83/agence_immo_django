from django.shortcuts import render,redirect
from django.http import HttpResponse
from appli_agence_immo.models import *


# Create your views here.

def main_acheteurs(request):
    return render(request, 'main_acheteurs.html')

def critere(request):
    return render(request, 'critere.html',
        {
            "pages":Acheteurs.objects.all(),
            "rien":Acheteurs.objects.count()==0,
            "biens":Bien_Immobiliers.objects.all()
        })