from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('weapon/', views.weapon, name='weapon'),
    path('armor/', views.armor, name='armor'),
    path('equipment/', views.equipment, name='equipment'),
    path('tools/', views.tools, name='tools'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
