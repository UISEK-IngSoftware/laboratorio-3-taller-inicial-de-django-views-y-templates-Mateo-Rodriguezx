from django.shortcuts import render

def index(request):
    pokemons = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle"]  
    return render(request, 'index.html', {
        'pokemons': pokemons
        })
def pokemons_details(request, pokemons):
    return render(request, "pokemons_details.html",{
        'pokemons': pokemons
        })