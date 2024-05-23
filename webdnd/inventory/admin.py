from django.contrib import admin
from .models import Weapon, Armor, Equipment, Tools

admin.site.register(Weapon),
admin.site.register(Armor),
admin.site.register(Equipment),
admin.site.register(Tools)
