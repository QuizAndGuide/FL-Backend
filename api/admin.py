from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


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


@admin.register(models.Classification)   
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ['team', 'points', 'wins', 'losses', 'draws']
    search_fields = ['team']
    ordering = ['points']


@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = [ 'player_id', 'team_id', 'nick']


@admin.register(models.SimplePlayer)
class SimplePlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick', 'name']
