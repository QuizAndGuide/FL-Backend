from typing import Any
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Round, Stats

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','is_staff','date_joined']


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user_id', 'phone', 'birth_date', 'membership']


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = [  'id','year', 'group', 'total_group', 'round',
                    'local', 'visitor', 'league_id', 'stadium', 'team1',
                    'team2', 'conference', 'dteam1', 'dteam2', 'numc',
                    'no_hour', 'local_abbr', 'visitor_abbr', 'competition_name',
                    'competition_id', 'split_league', 'type', 'type_id', 'playoffs',
                    'group_code', 'total_rounds', 'coef', 'cflag_local', 'cflag_visitor',
                    'local_shield', 'visitor_shield', 'extraTxt', 'schedule', 'date',
                    'hour', 'minute', 'local_goals', 'visitor_goals', 'result',
                    'live_minute', 'status', 'channels', 'winner', 'penaltis1', 'penaltis2' ]
        ordering = ['-schedule']
        
        
class RoundUpdaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = [  'year', 'group', 'total_group', 'round',
                    'local', 'visitor', 'league_id', 'stadium', 'team1',
                    'team2', 'conference', 'dteam1', 'dteam2', 'numc',
                    'no_hour', 'local_abbr', 'visitor_abbr', 'competition_name',
                    'competition_id', 'split_league', 'type', 'type_id', 'playoffs',
                    'group_code', 'total_rounds', 'coef', 'cflag_local', 'cflag_visitor',
                    'local_shield', 'visitor_shield', 'extraTxt', 'schedule', 'date',
                    'hour', 'minute', 'local_goals', 'visitor_goals', 'result',
                    'live_minute', 'status', 'channels', 'winner', 'penaltis1', 'penaltis2' ]
        ordering = ['-schedule']
        
        
        
class MatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = [ 'local', 'local_shield', 'visitor', 'visitor_shield', 'schedule' ]
        ordering = ['-schedule']
        
        
class StatsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stats
        fields = '__all__'

class MaxGoalersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stats
        fields = ['nick', 'player_image', 'team_name', 'goals']
        
        
# class AgendaSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Agenda
#         fields = '__all__'