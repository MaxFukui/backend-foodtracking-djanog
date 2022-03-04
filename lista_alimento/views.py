from django.shortcuts import render
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from .serializers import ComidaSerializer
from .models import ListaComida

# Create your views here.

#viesets provê a implementação para operações CRUD por padrão
#ver mais sobre serializer_class e queryset
class ListaComidaView(viewsets.ModelViewSet):
    serializer_class = ComidaSerializer
    queryset = ListaComida.objects.all()

    def create(self, request):
        request_load = request.data.dict()
        comida_encontrada = ListaComida.objects(comida=request_load['comida'])
        if(comida_encontrada.count() > 0):
            for i in comida_encontrada:
                i.update(set__calorias=float(request_load['calorias']))
                i.update(set__porcao=float(request_load['porcao']))
            return Response("Update Ok")
        nova_comida = ListaComida(comida=request_load['comida'].casefold(),
            calorias=request_load['calorias'], porcao=request_load['porcao'])
        nova_comida.save()
        return Response("ok")