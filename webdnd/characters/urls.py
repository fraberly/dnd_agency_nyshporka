from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.characters, name='characters'),
    path('character', views.character,
         name='character'),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)