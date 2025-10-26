from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemons<str:pokemons>/', views.pokemons_details, name='pokemons_details'),
]
