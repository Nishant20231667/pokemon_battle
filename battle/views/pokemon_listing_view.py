from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from battle.models import Pokemon
from battle.serializers import PokemonSerializer


class PokemonListView(APIView, PageNumberPagination):
    page_size = 10

    def get(self, request):
        pokemons = Pokemon.objects.all()
        results = self.paginate_queryset(pokemons, request, view=self)
        serializer = PokemonSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
