from django.contrib import admin
from .models import Worlds, Dice, Main, Mechanics

# Register your models here.
admin.site.register(Worlds)
admin.site.register(Main)
admin.site.register(Mechanics)
admin.site.register(Dice)

