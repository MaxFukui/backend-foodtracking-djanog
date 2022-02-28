from django.db import models
from mongoengine import *
connect("projeto_calorias")
# Create your models here.
class ListaComida(Document):
    meta = {'collection':'post_alimento',
        'allow_inheritance':True}
    comida = StringField(required=True, unique=True)
    calorias = FloatField(required=True)
    porcao = FloatField(required=True)

