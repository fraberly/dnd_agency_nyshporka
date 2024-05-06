from django.shortcuts import render


def characters(request):
    return render(request, 'characters/characters.html')


def character(request):
    return render(request, 'characters/character.html')
