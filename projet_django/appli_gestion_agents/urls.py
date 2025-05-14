from django.urls import path
from . import views

app_name = 'appli_gestion_agents'

urlpatterns = [
    path('main_agents', views.main_agents, name='main_agents'),
    path('port_vendeur', views.port_vendeur, name='port_vendeur'),
    path('port_acheteur', views.port_acheteur, name='port_acheteur'),
]