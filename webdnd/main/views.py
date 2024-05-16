from django.shortcuts import render
from .models import Worlds
# from django.http import HttpResponse

#
# def all_user(request):
#     return HttpResponse('Returning all user')


def home(request):
    data = {
        'title': 'Головна'
    }
    return render(request, 'main/home.html', data)


def about(request):
    data = {
        'title': 'Про нас'
    }
    return render(request, 'main/about.html', data)


def mechanics(request):
    data = {
        'title': 'Механіка'
    }
    return render(request, 'main/mechanics.html', data)


def world(request):
    worlds = Worlds.objects.all()
    return render(request,
                  'main/world.html',
                  {'worlds': worlds}
                  )


