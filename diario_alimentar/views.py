from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from .serializers import DiarioAlimentarSerializer
from .models import DiarioAlimentar

# Create your views here.

#viesets provê a implementação para operações CRUD por padrão
#ver mais sobre serializer_class e queryset
class DiarioAlimentarView(viewsets.ModelViewSet):
    serializer_class = DiarioAlimentarSerializer
    queryset = DiarioAlimentar.objects.all()
# Create your views here.
