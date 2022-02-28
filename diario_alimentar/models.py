from mongoengine import *
from lista_alimento import models
import datetime
# Create your models here.
connect("projeto_calorias")
# Create your models here.

register_connection('ListaAlimento')
class DiarioAlimentar(Document):
    meta = {'collection':'post_diario_alimentar'}
    # comida = EmbeddedDocumentField('ListaAlimento', required=True)
    comida = ReferenceField(models.ListaComida)
    porcao = FloatField(required=True)
    dia = DateTimeField(default=datetime.datetime.now)