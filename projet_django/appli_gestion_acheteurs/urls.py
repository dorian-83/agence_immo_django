from django.urls import path
from . import views

app_name = 'appli_gestion_acheteurs'

urlpatterns = [
    path('main_acheteurs', views.main_acheteurs, name='main_acheteurs'),
    path('critere', views.critere, name='critere'),
    path('suivi_bien', views.suivi_bien, name='suivi_bien'),
    path('gestion_retour', views.gestion_retour, name='gestion_retour'),
]