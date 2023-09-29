from django.shortcuts import render


def index(request):
    return render(request, 'tailleur_core/index.html')
