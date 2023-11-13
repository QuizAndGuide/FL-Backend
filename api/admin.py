from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models
import json


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

   
@admin.register(models.Jornada)
class NextGames(admin.ModelAdmin):
    list_display = [ 'year', 'id', 'group', 'total_group', 'round',
                    'local', 'visitor', 'league_id', 'stadium', 'team1',
                    'team2', 'conference', 'dteam1', 'dteam2', 'numc',
                    'no_hour', 'local_abbr', 'visitor_abbr', 'competition_name',
                    'competition_id', 'split_league', 'type', 'type_id', 'playoffs',
                    'group_code', 'total_rounds', 'coef', 'cflag_local', 'cflag_visitor',
                    'local_shield', 'visitor_shield', 'extraTxt', 'schedule', 'date',
                    'hour', 'minute', 'local_goals', 'visitor_goals', 'result',
                    'live_minute', 'status', 'channels', 'winner', 'penaltis1', 'penaltis2' ]
    ordering = ['-schedule']