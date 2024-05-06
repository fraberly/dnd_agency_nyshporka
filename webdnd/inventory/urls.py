from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('/money', views.money, name='money'),
    path('/weapon', views.weapon, name='weapon'),
    path('/armor', views.armor, name='armor'),
    path('/equipment', views.equipment, name='equipment'),
    path('/tools', views.tools, name='tools'),
]
