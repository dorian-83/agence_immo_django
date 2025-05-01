from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main', views.main, name='main'),
    path('ajouter_acheteur', views.ajouter_acheteur, name='ajouter_acheteur'),
    path('ajouter_vendeur', views.ajouter_vendeur, name='ajouter_vendeur'),
    path('ajouter_agent', views.ajouter_agent, name='ajouter_agent'),
    path('ajouter_bien', views.ajouter_bien, name='ajouter_bien'), 
]