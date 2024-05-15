from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mechanics/', views.mechanics, name='mechanics'),
    path('world/', views.world, name='world'),
]