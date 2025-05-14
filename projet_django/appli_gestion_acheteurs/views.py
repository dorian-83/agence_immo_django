from django.shortcuts import render,redirect
from django.http import HttpResponse
from appli_agence_immo.models import *
from .forms import SuiviForm,GestionForm


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

def gestion_retour(request):
    if request.method == "POST":
        form = GestionForm(request.POST)
        if form.is_valid():
            id_bien = form.cleaned_data['id_bien']            #on a l'id du bien
            nom_acheteur = form.cleaned_data['nom_acheteur']  #on a le nom de l'acheteur
            bien_achete = form.cleaned_data['bien_achete']
            acheteur=Acheteurs.objects.get(nom=nom_acheteur)  #on a la ligne de l'acheteur dans la table acheteur
            id_acheteur=acheteur.id_acheteur                  # on a l'id de l'acheteur
            instance_modif=Achat.objects.get(id_acheteur=id_acheteur,id_bien=id_bien)    #instance que l'on veut modifier
            form=GestionForm(request.POST,instance=instance_modif)
            form.save()
            bien_modif=Bien_Immobiliers.objects.get(id_bien=id_bien)  #bien dont l'état doit être modifié
            if bien_achete==True:
                bien_modif.etat="acheté"
                bien_modif.save()
            form=GestionForm()
            return render(request,"gestion_retour.html",
                {
                    'form': form,
                    "table":Achat.objects.select_related("id_acheteur"),
                    "rien":Achat.objects.count()==0,
                })
    else:
        form=GestionForm()
    return render(request, 'modifier_fait.html',{'form': form})  


