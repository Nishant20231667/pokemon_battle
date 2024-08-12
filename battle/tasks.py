from celery import shared_task
from .models import Battle, Pokemon
from django.core.exceptions import ObjectDoesNotExist

@shared_task
def start_battle_task(battle_id, pokemon_a_name, pokemon_b_name):
    try:
        battle = Battle.objects.get(id=battle_id)

        pokemon_a_data = Pokemon.objects.get(name__iexact=pokemon_a_name)
        pokemon_b_data = Pokemon.objects.get(name__iexact=pokemon_b_name)

        attack_a = pokemon_a_data.attack
        type1_a = pokemon_a_data.type1
        type2_a = pokemon_a_data.type2

        attack_b = pokemon_b_data.attack
        type1_b = pokemon_b_data.type1
        type2_b = pokemon_b_data.type2

        against_a_type1 = getattr(pokemon_b_data, f"against_{type1_a}", 1)
        against_a_type2 = getattr(pokemon_b_data, f"against_{type2_a}", 1)

        against_b_type1 = getattr(pokemon_a_data, f"against_{type1_b}", 1)
        against_b_type2 = getattr(pokemon_a_data, f"against_{type2_b}", 1)

        damage_a_to_b = (attack_a / 200) * 100 - (((against_a_type1 / 4) * 100) + ((against_a_type2 / 4) * 100))

        damage_b_to_a = (attack_b / 200) * 100 - (((against_b_type1 / 4) * 100) + ((against_b_type2 / 4) * 100))

        if damage_a_to_b > damage_b_to_a:
            winner = pokemon_a_data.name
            margin = damage_a_to_b - damage_b_to_a
        elif damage_b_to_a > damage_a_to_b:
            winner = pokemon_b_data.name
            margin = damage_b_to_a - damage_a_to_b
        else:
            winner = "Draw"
            margin = 0

        battle.status = 'BATTLE_COMPLETED'
        battle.result = {
            'winnerName': winner,
            'wonByMargin': margin
        }
        battle.save()

    except ObjectDoesNotExist:
        if 'battle' in locals():
            battle.status = 'BATTLE_FAILED'
            battle.result = None
            battle.save()
    except Exception as e:
        if 'battle' in locals():
            battle.status = 'BATTLE_FAILED'
            battle.result = None
            battle.save()
