from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from .serializers import ComidaSerializer
from .models import ListaComida

# Create your views here.

#viesets provê a implementação para operações CRUD por padrão
#ver mais sobre serializer_class e queryset
class ListaComidaView(viewsets.ModelViewSet):
    serializer_class = ComidaSerializer
    queryset = ListaComida.objects.all()