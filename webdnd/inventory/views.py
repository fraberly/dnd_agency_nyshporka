from django.shortcuts import render
from .models import Weapon, Armor, Equipment, Tools


def inventory(request):
    weapon = Weapon.objects.all().order_by('name')
    armor = Armor.objects.all().order_by('name')
    equipment = Equipment.objects.all().order_by('name')
    tools = Tools.objects.all().order_by('name')
    data = {
        'weapon': weapon,
        'armor': armor,
        'equipment': equipment,
        'tools': tools }
    return render(request,
                  'inventory/inventory.html', data)



def weapon(request):
    weapon = Weapon.objects.all().order_by('name')
    return render(request,
                  'inventory/weapon.html',
                  {'weapon': weapon})


def armor(request):
    armor = Armor.objects.all().order_by('name')
    return render(request,
                  'inventory/armor.html',
                  {'armor': armor})


def equipment(request):
    equipment = Equipment.objects.all().order_by('name')
    return render(request,
                  'inventory/equipment.html',
                  {'equipment': equipment})


def tools(request):
    tools = Tools.objects.all().order_by('name')
    return render(request, 'inventory/tools.html',
                  {'tools': tools})
