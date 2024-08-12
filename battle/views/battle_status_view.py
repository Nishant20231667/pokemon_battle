from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from battle.serializers import BattleStatusSerializer
from battle.models import Battle

class BattleStatusView(APIView):
    def post(self, request):
        serializer = BattleStatusSerializer(data=request.data)
        if serializer.is_valid():
            battle_id = serializer.validated_data['battle_id']
            
            try:
                battle = Battle.objects.get(id=battle_id)
                response_data = {
                    "status": battle.status,
                    "result": battle.result
                }
                return Response(response_data, status=status.HTTP_200_OK)
            except Battle.DoesNotExist:
                return Response({"error": "Battle not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
