from django.urls import path
from . import views

app_name = 'appli_gestion_vendeurs'

urlpatterns = [
    path('main_vendeurs', views.main_vendeurs, name='main_vendeurs'),
    path('etat_bien', views.etat_bien, name='etat_bien'),
]