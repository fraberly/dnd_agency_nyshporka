from django.shortcuts import render


def inventory(request):
    return render(request, 'inventory/inventory.html')


def money(request):
    return render(request, 'inventory/money.html')


def weapon(request):
    return render(request, 'inventory/weapon.html')


def armor(request):
    return render(request, 'inventory/armor.html')


def equipment(request):
    return render(request, 'inventory/equipment.html')


def tools(request):
    return render(request, 'inventory/tools.html')
