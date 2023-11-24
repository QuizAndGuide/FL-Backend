from typing import Any
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, RoundMatch, Stats, MonthMatch
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','is_staff','date_joined']


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user_id', 'phone', 'birth_date', 'membership']



class RoundMatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RoundMatch
        fields = '__all__'
        ordering = ['-schedule']

    def to_internal_value(self, data):
        if 'date' in data:
            data['date'] = datetime.strptime(data['date'], '%Y/%m/%d').date()
        return super().to_internal_value(data)

    def to_representation(self, instance):
        if instance.status == -1:
            fields = ['local', 'local_shield', 'visitor', 'visitor_shield', 'schedule']
        elif instance.status == 1:
            fields = ['local', 'local_shield', 'visitor', 'visitor_shield', 'date', 'result']
        else:
            fields = []

        ret = {}
        for field in fields:
            ret[field] = getattr(instance, field)

        return ret

        
class StatsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stats
        fields = '__all__'

    def to_representation(self, instance):    
        fields = ['nick', 'player_image', 'team_name', 'team_shield', 'goals']
        ret = {}
        for field in fields:
            ret[field] = getattr(instance, field)

        return ret
        
        
class MonthMatchesinputSerializer(serializers.ModelSerializer):

    class Meta:
        model = MonthMatch
        fields = '__all__'


class MonthMatchesUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MonthMatch
        fields = ['team1', 'team2', 'r1', 'r2', 'p1', 'p2', 'status',
                  'round', 'shedule', 'league_id', 't1', 't2', 'id_t1',
                  'id_t2', 'finished', 't1_short', 't2_short', 'group_code',
                  'categoryId', 'year', 'cc1', 'cc2']
        
        
class NextMonthMatchesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MonthMatch
        fields = ['team1', 'team2', 'shedule']
        