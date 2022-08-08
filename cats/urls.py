from django.urls import path
from . import views

urlpatterns = [
    path('', views.getCats, name='home'),
    # path('sendcat', views.sendCat, name='send'),
    path('breeds/<slug:breed>', views.displayCats, name='beed')
]