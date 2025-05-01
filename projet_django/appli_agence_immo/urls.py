from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name='main'),
    path('ajouter_acheteur', views.ajouter_acheteur, name='ajouter_acheteur'), 
]