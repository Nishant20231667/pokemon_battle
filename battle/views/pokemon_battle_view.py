import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from battle.serializers import BattleSerializer
from battle.tasks import start_battle_task
from battle.models import Battle, Pokemon

class StartBattleView(APIView):
    def post(self, request):
        serializer = BattleSerializer(data=request.data)
        if serializer.is_valid():
            pokemon_a_name = serializer.validated_data['pokemon_a']
            pokemon_b_name = serializer.validated_data['pokemon_b']

            pokemon_a = Pokemon.objects.get(name__iexact=pokemon_a_name)
            pokemon_b = Pokemon.objects.get(name__iexact=pokemon_b_name)

            # Create a new battle record with a generated UUID
            battle = Battle.objects.create(
                id=uuid.uuid4(),
                pokemon_a=pokemon_a,
                pokemon_b=pokemon_b,
                status='BATTLE_STARTED'
            )
            
            # Pass the battle ID and Pokémon names to the task
            start_battle_task.delay(str(battle.id), pokemon_a.name, pokemon_b.name)
            
            return Response({"battle_id": battle.id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
