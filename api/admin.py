from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models
from .serializers import TableSerializer
import json


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

   
@admin.register(models.Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ['basealias', 'city']
    search_fields = ['basealias']


# @admin.register(models.Clasificacion)   
# class ClassificationAdmin(admin.ModelAdmin):
#     tabla = []
#     queryset =  models.Clasificacion.objects.all().last()
#     for i in queryset.table:
#         tabla.append(str(i))
#     list_display = tabla
    

@admin.register(models.Clasificacion)
class ClassificationAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        # Obtén la última instancia de Clasificacion en tiempo de ejecución
        last_instance = models.Clasificacion.objects.all().last()
        
        # Asegúrate de que 'table' no sea None
        if last_instance.table:
            # Obtén las claves de un diccionario de la primera entrada (si es una lista de diccionarios)
            first_entry = last_instance.table[0]
            fields_to_display = first_entry.keys() if isinstance(first_entry, dict) else []
        else:
            fields_to_display = []  # En caso de que 'table' esté vacío o sea None

        return fields_to_display
    


@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = [ 'player_id', 'team_id', 'nick']


@admin.register(models.SimplePlayer)
class SimplePlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick', 'name']
