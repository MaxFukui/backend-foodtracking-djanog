# from rest_framework import serializers
from rest_framework_mongoengine import serializers
from .models import DiarioAlimentar

# Serializaer é reponsável por converter para o modelo Json
class DiarioAlimentarSerializer(serializers.DocumentSerializer):
    class Meta:
        model = DiarioAlimentar
        fields = ('comida', 'calorias', 'porcao')