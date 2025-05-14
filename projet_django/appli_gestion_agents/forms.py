from django import forms
from django.forms import ModelForm
from appli_agence_immo.models import *

class AgentForm(forms.Form):
    nom_agent=forms.CharField(label="Nom de l'agent")