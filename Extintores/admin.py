from django.contrib import admin
from .models import Extintor
# Register your models here.
@admin.register(Extintor)
class extintoradmin(admin.ModelAdmin):
    list_display = ('tagid','fecha_ultima_mantencion','fecha_sig_mantencion')
#admin.site.register(extintoradmin)