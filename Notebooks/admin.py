from django.contrib import admin
from .models import Notebook
# Register your models here.
@admin.register(Notebook)
class notebookadmin(admin.ModelAdmin):
    list_display = ('tagid','fecha_ultima_mantencion','SO')