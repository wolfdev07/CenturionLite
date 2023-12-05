from rest_framework import serializers
from CenturionApi.models import State, City, PostalCode, Settlement


class PostalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalCode
        fields = '__all__'
        #read_only_fields = ('all',)



class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = '__all__'



class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'



class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'