# from rest_framework import serializers
from rest_framework_mongoengine import serializers
from .models import ListaComida

# Serializaer é reponsável por converter para o modelo Json
class ComidaSerializer(serializers.DocumentSerializer):
    class Meta:
        model = ListaComida
        fields = ('comida', 'calorias', 'porcao')