from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mechanics/', views.mechanics, name='mechanics'),
    path('world/', views.world, name='world'),
    path('admin/', admin.site.urls, name='admin')
]