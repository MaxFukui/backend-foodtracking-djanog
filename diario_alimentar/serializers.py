# from rest_framework import serializers
from rest_framework_mongoengine import serializers
from .models import DiarioAlimentar, CaloriasTotais
from lista_alimento.serializers import ComidaSerializer

# Serializaer é reponsável por converter para o modelo Json
class DiarioAlimentarSerializer(serializers.DocumentSerializer):
    # comida = serializers.StringRelatedField(many=True)
    comida=ComidaSerializer(many=False)
    class Meta:
        model = DiarioAlimentar
        fields = ["comida", "porcao", "dia"]

class CaloriasTotaisSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CaloriasTotais
        fields = ('calorias', 'dia')

class GetDiarioAlimentarSerializer(serializers.DocumentSerializer):
    comida=ComidaSerializer(many=True)
    class Meta:
        model = DiarioAlimentar
        fields = "__all__"