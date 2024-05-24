from django.shortcuts import render
from .models import Characters


def characters(request):
    charactes = Characters.objects.all()
    return render(request, 'characters/characters.html',
                  {'charactes': charactes})


def character(request):
    charactes = Characters.objects.all()
    return render(request, 'characters/character.html',{'charactes': charactes})
