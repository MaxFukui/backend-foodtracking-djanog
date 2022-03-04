from mongoengine import *
from lista_alimento import models
import datetime
# Create your models here.
connect("projeto_calorias")
# Create your models here.

register_connection('ListaAlimento')
class DiarioAlimentar(Document):
    meta = {'collection':'post_diario_alimentar', 'ordering':'dia'}
    # comida = EmbeddedDocumentField('ListaAlimento', required=True)
    comida = ReferenceField(models.ListaComida)
    porcao = FloatField(required=True)
    dia = DateTimeField(default=datetime.datetime.now)

class CaloriasTotais(Document):
    meta = {'collection':'calorias_totais_dia', 'ordering':'dia'}
    calorias = FloatField()
    dia = DateTimeField(default=datetime.datetime.now)