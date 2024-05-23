from django.shortcuts import render
from .models import Weapon, Armor, Equipment, Tools


def inventory(request):

    weapon = Weapon.objects.all()
    armor = Armor.objects.all()
    equipment = Equipment.objects.all()
    tools = Tools.objects.all()

    data = {
        'weapon': weapon,
        'armor': armor,
        'equipment': equipment,
        'tools': tools
    }

    return render(request, 'inventory/inventory.html',
                  data)



def weapon(request):
    weapon = Weapon.objects.all()
    return render(request, 'inventory/weapon.html',
                  {'weapon': weapon})


def armor(request):
    armor = Armor.objects.all()
    return render(request, 'inventory/armor.html',
                  {'armor': armor})


def equipment(request):
    equipment = Equipment.objects.all()
    return render(request, 'inventory/equipment.html',
                  {'equipment': equipment})


def tools(request):
    tools = Tools.objects.all()
    return render(request, 'inventory/tools.html',
                  {'tools': tools})
