from django.shortcuts import render
from .models import Worlds, Main, Mechanics
# from django.http import HttpResponse

#
# def all_user(request):
#     return HttpResponse('Returning all user')


def home(request):
    mains = Main.objects.all()
    return render(request, 'main/home.html',
                  {'mains': mains})


def mechanics(request):
    mechanics = Mechanics.objects.all()
    return render(request, 'main/mechanics.html', {'mechanics': mechanics})


def world(request):
    worlds = Worlds.objects.all()
    return render(request,
                  'main/world.html',
                  {'worlds': worlds}
                  )


