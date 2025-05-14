from django.shortcuts import render,redirect
from django.http import HttpResponse
from appli_agence_immo.models import *
from .forms import AgentForm


# Create your views here.

def main_agents(request):
    return render(request, 'main_agents.html')

def port_vendeur(request):
    if request.method == "POST":
        form=AgentForm(request.POST)
        if form.is_valid():
            nom_agent = form.cleaned_data['nom_agent']
            table=Achat.objects.select_related("id_agent","id_acheteur","id_bien").filter(id_agent__nom = nom_agent)
            ids_deja_vus = set()
            biens_uniques = []
            for achat in table:
                if achat.id_bien not in ids_deja_vus:
                    biens_uniques.append(achat)
                    ids_deja_vus.add(achat.id_bien)
            return render(request,"port_vendeur.html",
                {
                    "table":biens_uniques,
                    "rien":len(biens_uniques)==0,
                })
    else:
        form=AgentForm()
    return render(request, 'entrer_agent.html', {'form': form})



def port_acheteur(request):
    if request.method == "POST":
        form=AgentForm(request.POST)
        if form.is_valid():
            nom_agent = form.cleaned_data['nom_agent']
            table=Achat.objects.select_related("id_agent","id_acheteur").filter(id_agent__nom = nom_agent)
            ids_deja_vus = set()
            acheteurs_uniques = []
            for achat in table:
                if achat.id_acheteur not in ids_deja_vus:
                    acheteurs_uniques.append(achat)
                    ids_deja_vus.add(achat.id_acheteur)
            return render(request,"port_acheteur.html",
                {
                    "table":acheteurs_uniques,
                    "rien":len(acheteurs_uniques)==0,
                })
    else:
        form=AgentForm()
    return render(request, 'entrer_agent.html', {'form': form})


""""
agent = Agent_immo.objects.get(nom=nom_agent)
            id_agent=agent.id_agent
"""



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