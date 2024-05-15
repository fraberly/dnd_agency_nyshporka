from django.urls import path
from . import views

urlpatterns = [
    path('', views.characters, name='characters'),
    path('character', views.character, name='character'),
]