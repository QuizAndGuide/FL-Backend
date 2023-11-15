from typing import Any
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Jornada, Agenda

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','is_staff','date_joined']


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user_id', 'phone', 'birth_date', 'membership']


class JornadaSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date'] = instance.date.strftime('%Y-%m-%d')
        return representation
    class Meta:
        model = Jornada
        fields = [ 'year', 'id', 'group', 'total_group', 'round',
                    'local', 'visitor', 'league_id', 'stadium', 'team1',
                    'team2', 'conference', 'dteam1', 'dteam2', 'numc',
                    'no_hour', 'local_abbr', 'visitor_abbr', 'competition_name',
                    'competition_id', 'split_league', 'type', 'type_id', 'playoffs',
                    'group_code', 'total_rounds', 'coef', 'cflag_local', 'cflag_visitor',
                    'local_shield', 'visitor_shield', 'extraTxt', 'schedule', 'date',
                    'hour', 'minute', 'local_goals', 'visitor_goals', 'result',
                    'live_minute', 'status', 'channels', 'winner', 'penaltis1', 'penaltis2' ]
        ordering = ['-schedule']
        
        
        
class PartidosSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date'] = instance.date.strftime('%Y-%m-%d')
        return representation
    class Meta:
        model = Jornada
        fields = [ 'local', 'visitor', 'schedule' ]
        ordering = ['-schedule']
        

class AgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agenda
        fields = '__all__'