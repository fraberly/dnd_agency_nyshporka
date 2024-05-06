from django.shortcuts import render


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
    data = {
        'title': 'Світ'
    }
    return render(request, 'main/world.html', data)


