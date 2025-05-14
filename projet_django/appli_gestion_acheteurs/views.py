from django.shortcuts import render,redirect
from django.http import HttpResponse
from appli_agence_immo.models import *
from .forms import SuiviForm


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

def suivi_bien(request):
    if request.method == "POST":
        form = SuiviForm(request.POST)
        if form.is_valid():
            nom_acheteur = form.cleaned_data['nom_acheteur']
            return render(request,"suivi_bien.html",
                {
                    "nom_acheteur":nom_acheteur,
                    "com":Achat.objects.select_related("id_acheteur","id_bien").filter(id_acheteur__nom = nom_acheteur),
                    "visite":Achat.objects.select_related("id_acheteur","id_bien").filter(id_acheteur__nom=nom_acheteur,bien_visite=1),
                    "achete":Achat.objects.select_related("id_acheteur","id_bien").filter(id_acheteur__nom=nom_acheteur,bien_achete=1),
                    "rien":Achat.objects.count()==0,
                })
    else:
        form=SuiviForm()
    return render(request, 'entrer_acheteur.html', {'form': form})

