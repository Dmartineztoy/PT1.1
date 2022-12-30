from django.db import models

# Create your models here.
class Extintor(models.Model):
    tagid = models.CharField(max_length=50)
    fecha_ultima_mantencion = models.DateField()
    fecha_sig_mantencion = models.DateField()
    def __str__(self):
        texto="{0} {1} {2}"
        return texto.format(self.tagid, self.fecha_ultima_mantencion, self.fecha_sig_mantencion)