from django.urls import path
from . import views

urlpatterns = [
    path('', views.getCats, name='home'),
    path('topten', views.topten, name='tt'),
    path('breeds/<slug:breed>', views.displayCats, name='beed')
]