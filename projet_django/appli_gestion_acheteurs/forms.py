from django import forms
from django.forms import ModelForm
from appli_agence_immo.models import *

class SuiviForm(forms.Form):
    nom_acheteur=forms.CharField(label="Nom de l'acheteur")

class GestionForm(forms.ModelForm):
    nom_acheteur=forms.CharField(label="Nom de l'acheteur")
    id_bien=forms.IntegerField(label="Référence du bien")
    class Meta:
        model = Achat
        fields = ['bien_visite', 'bien_achete']