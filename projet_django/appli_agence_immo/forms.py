from django import forms
from django.forms import ModelForm
from .models import Acheteurs

class AcheteursForm(ModelForm):
    class Meta:
        model = Acheteurs
        fields = "__all__"