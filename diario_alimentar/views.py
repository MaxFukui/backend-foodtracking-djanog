from tkinter import CASCADE
from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response

from .serializers import DiarioAlimentarSerializer, CaloriasTotaisSerializer, GetDiarioAlimentarSerializer
from .models import DiarioAlimentar, CaloriasTotais
from lista_alimento.models import ListaComida
from datetime import date

# Create your views here.

#viesets provê a implementação para operações CRUD por padrão
#ver mais sobre serializer_class e queryset
class DiarioAlimentarView(viewsets.ModelViewSet):
    serializer_class = DiarioAlimentarSerializer
    queryset = DiarioAlimentar.objects.all()

    def create(self, request):
        request_load = request.data.dict()
        comida_lista_comida = ListaComida.objects(comida = request_load['comida'])
        print(comida_lista_comida[0].id)
        print(request_load)
        diarioAlimentar = DiarioAlimentar(porcao=request_load['porcao'],
            dia=date.today())
        diarioAlimentar.comida = comida_lista_comida[0].id
        diarioAlimentar.save()
        return Response("ok")

    def list(self, resquest):
        lista_alimentos_hoje = DiarioAlimentar.objects(dia=date.today())
        serializer = DiarioAlimentarSerializer(lista_alimentos_hoje, many=True)
        return Response(serializer.data)
        # lista_alimentos_hoje = DiarioAlimentar.objects(dia=date.today())
        # serializer = GetDiarioAlimentarSerializer(lista_alimentos_hoje, many=True)
        # return Response(serializer.data)

# Create your views here.

class CaloriasTotaisView(viewsets.ModelViewSet):
    serializer_class = CaloriasTotaisSerializer
    queryset = CaloriasTotais.objects.all()
    def list(self, request):
        lista_alimentos_hoje = DiarioAlimentar.objects(dia=date.today())
        calorias_totais = 0
        for i in lista_alimentos_hoje:
            alimento = ListaComida.objects(id=i.comida.id)[0]
            ## caloria comi/ porcao comi = caloria alimento/ pocao alimento
            calorias_totais+= (i.porcao * alimento.calorias/alimento.porcao)
        formater = "{0:.2f}"  
        calorias_dia = CaloriasTotais(calorias=float(formater.format(calorias_totais)))
        serializerCalorias = CaloriasTotaisSerializer(calorias_dia)
        return Response(serializerCalorias.data)