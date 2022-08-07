from django.urls import path
from . import views

urlpatterns = [
    path('', views.getCats, name='home'),
    path('breeds/<slug:breed>', views.displayCats, name='beed')
]