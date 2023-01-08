from django.db import models
from .choices import edificios
import datetime
# Create your models here.
class TagRFID(models.Model):
    tagid = models.CharField(max_length=6,primary_key=True,default='1')
    fecha_ultima_mantencion = models.DateField(default=datetime.date.today)
    edificio=models.CharField(max_length=3, choices=edificios,default='A1')
    class Meta:
        abstract = True
        
class Extintor(TagRFID):
    fecha_sig_mantencion = models.DateField()
    def __str__(self):
        texto="{0} {1} {2} {3}"
        return texto.format(self.tagid, self.fecha_ultima_mantencion, self.fecha_sig_mantencion, self.edificio)