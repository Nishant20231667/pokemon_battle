from rest_framework import serializers
from .models import Pokemon
from difflib import SequenceMatcher


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = "__all__"


class BattleSerializer(serializers.Serializer):
    pokemon_a = serializers.CharField()
    pokemon_b = serializers.CharField()

    def validate(self, data):
        pokemon_a_name = data["pokemon_a"].strip().lower()
        pokemon_b_name = data["pokemon_b"].strip().lower()

        pokemon_a, pokemon_a_mistakes = self.get_closest_pokemon_name(pokemon_a_name)
        pokemon_b, pokemon_b_mistakes = self.get_closest_pokemon_name(pokemon_b_name)

        if not pokemon_a or not pokemon_b:
            raise serializers.ValidationError(
                f"Pokémon '{data['pokemon_a']}' or '{data['pokemon_b']}' not found."
            )

        if pokemon_a_mistakes > 1 or pokemon_b_mistakes > 1:
            raise serializers.ValidationError(
                "More than one spelling mistake found in Pokémon name."
            )

        data["pokemon_a_obj"] = pokemon_a
        data["pokemon_b_obj"] = pokemon_b

        return data

    def get_closest_pokemon_name(self, input_name):
        best_match = None
        best_ratio = 0.0
        best_mistakes = float("inf")

        for pokemon in Pokemon.objects.all():
            ratio = SequenceMatcher(None, input_name, pokemon.name.lower()).ratio()
            mistakes = len(pokemon.name) - len(input_name) + round((1 - ratio) * len(pokemon.name))
            
            if ratio > best_ratio or (ratio == best_ratio and mistakes < best_mistakes):
                best_match = pokemon
                best_ratio = ratio
                best_mistakes = mistakes

        return best_match, best_mistakes

class BattleStatusSerializer(serializers.Serializer):
    battle_id = serializers.UUIDField()

    def validate_battle_id(self, value):
        from .models import Battle

        if not Battle.objects.filter(id=value).exists():
            raise serializers.ValidationError("Battle ID not found.")
        return value
