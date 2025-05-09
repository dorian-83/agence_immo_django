from django.shortcuts import render, redirect
from django.http import HttpResponse
from appli_agence_immo.models import *
from .forms import ListRdvForm

# Create your views here.

def main_vendeurs(request):
    return render(request, 'main_vendeurs.html')


def etat_bien(request):
    return render(request, 'print_bien.html',
        {
            "pages":Bien_Immobiliers.objects.all(),
            "rien":Bien_Immobiliers.objects.count()==0
        })

def list_rdv(request):
    if request.method == "POST":
        form = ListRdvForm(request.POST)
        if form.is_valid():
            nom_vendeur = form.cleaned_data['nom_vendeur']
            return render(request,"list_rdv.html",
                {
                    "pages":Rendez_Vous.objects.select_related("id_vendeur","id_bien").filter(id_vendeur__nom=nom_vendeur),
                    "rien":Rendez_Vous.objects.count()==0
                })
    else:
        form=ListRdvForm()
    return render(request, 'entrer_vendeur.html', {'form': form})




#table1.objects.select_related("nom de la relation clé étrangère").filter

#ca fait une table avec tous les objets dans table1 et table2 ca fait un inner
#join sur les clés étrangères

#et filter c'est un where
