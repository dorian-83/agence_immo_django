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

class AgentForm(ModelForm):
    class Meta:
        model = Agent_immo
        fields = "__all__"

class BienForm(ModelForm):
    class Meta:
        model = Bien_Immobiliers
        fields = "__all__"