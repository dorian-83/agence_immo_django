from django.urls import path
from . import views

app_name = 'appli_gestion_acheteurs'

urlpatterns = [
    path('main_acheteurs', views.main_acheteurs, name='main_acheteurs'),
]