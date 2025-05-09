from django.shortcuts import render

# Create your views here.

def main_acheteurs(request):
    return render(request, 'main_acheteurs.html')