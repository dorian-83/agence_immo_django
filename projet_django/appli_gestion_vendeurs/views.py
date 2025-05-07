from django.shortcuts import render, redirect
from django.http import HttpResponse
from appli_agence_immo.models import *

# Create your views here.

def main_vendeurs(request):
    return render(request, 'main_vendeurs.html')


def etat_bien(request):
    return render(request, 'print_bien.html',
        {
            "pages":Bien_Immobiliers.objects.all(),
            "rien":Bien_Immobiliers.objects.count()==0
        })




#table1.objects.select_related("table2").filter


#ca fait une table avec tous les objets dans table1 et table2 ca fait un inner
#join sur les clés étrangères

#et filter c'est un where

"""
def pages(request):
    return render(request, 'pages.tmpl', 
        {                                          
            'pages': Client.objects.all(),
            'nb': Client.objects.count(),
            'rien': Client.objects.count()==0
        })
"""

