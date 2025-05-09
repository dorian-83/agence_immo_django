from django import forms
from django.forms import ModelForm
from .models import *

class AcheteursForm(ModelForm):
    class Meta:
        model = Acheteurs
        fields = "__all__"

class VendeursForm(ModelForm):
    class Meta:
        model = Vendeurs
        fields = "__all__"

class AgentsForm(ModelForm):
    class Meta:
        model = Agent_immo
        fields = "__all__"

class BiensForm(ModelForm):
    class Meta:
        model = Bien_Immobiliers
        fields = "__all__"

class RdvForm(ModelForm):
    class Meta:
        model = Rendez_Vous
        fields = "__all__"

class AchatForm(ModelForm):
    class Meta:
        model = Achat
        fields = "__all__"