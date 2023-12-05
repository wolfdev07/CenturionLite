from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from CenturionApi.models import PostalCode, Settlement
from CenturionApi.serializers import SettlementSerializer, CitySerializer, StateSerializer

# BUSCAR ASENTAMIENTO POR CODIGO POSTAL
@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def get_postal_code(request, code, format=str):
    try:
        postal_code = PostalCode.objects.get(code=code)
        settlements = Settlement.objects.filter(postal_code=postal_code)

        # Obtén la ciudad (municipio) relacionada con el código postal
        city = postal_code.city

        # Obtén el estado relacionado con la ciudad
        state = city.state

        # Serializa los datos
        serializer = {
            "settlements": SettlementSerializer(settlements, many=True).data,
            "city": CitySerializer(city).data,
            "state": StateSerializer(state).data,
        }

        return Response(serializer)

    except PostalCode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)