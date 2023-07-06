from django.shortcuts import render

from .models import Place, Client


def index(request):
    place = Place.objects.all()
    client = Client.objects.all()
    return render(request, 'index.html', {'place': place, 'client': client})
