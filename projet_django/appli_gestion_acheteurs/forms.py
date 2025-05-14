from django import forms
from django.forms import ModelForm
from appli_agence_immo.models import *

class SuiviForm(forms.Form):
    nom_acheteur=forms.CharField(label="Nom de l'acheteur")