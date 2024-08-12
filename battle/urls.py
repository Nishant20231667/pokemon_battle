from django.urls import path
from .views import PokemonListView, StartBattleView, BattleStatusView

urlpatterns = [
    path("pokemon/", PokemonListView.as_view(), name="pokemon-list"),
    path("battle/", StartBattleView.as_view(), name="battle"),
    path("battle_status/", BattleStatusView.as_view(), name="battle-status"),
]
