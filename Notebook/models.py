from django.db import models
from Extintor.choices import edificios
from Extintor.models import TagRFID
# Create your models here.
class Notebook(TagRFID):
    SO = models.CharField(max_length=10)
    def __str__(self):
        texto="{0} {1} {2} {3}"
        return texto.format(self.tagid, self.fecha_ultima_mantencion, self.SO, self.edificio)