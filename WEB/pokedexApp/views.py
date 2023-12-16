from typing import Any
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.

class Pokedex(ListView):
    model = Pokemon
    template_name = 'pokedexApp/pokedex.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        
        context['pokemones'] = Pokemon.objects.all
         
        return context

class PokemonDetalles(DetailView):
    model = Pokemon
    template_name = 'pokedexApp/pokemonDetalle.html'
