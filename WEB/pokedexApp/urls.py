from django.urls import path
from .views import *

urlpatterns = [
    path('', Pokedex.as_view(), name='pokedex'),
    path('pokemon/<int:pk>', PokemonDetalles.as_view(), name='detalles'),
]
