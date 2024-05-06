from django.urls import path
from . import views

urlpatterns = [
    path('', views.characters, name='characters'),
    path('/', views.character, name='character'),
]