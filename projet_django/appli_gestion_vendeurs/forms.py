from django import forms
from django.forms import ModelForm
from appli_agence_immo.models import *

class ListRdvForm(forms.Form):
    nom_vendeur=forms.CharField(label="Nom du vendeur")