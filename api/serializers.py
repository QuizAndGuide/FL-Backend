from typing import Any
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Clasificacion, Teams, Player, SimplePlayer, Table, Legend, Info, Legends

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        

class SimplePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimplePlayer
        fields = '__all__'
    
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
        
class LegendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legend
        fields = '__all__'

class LegendsSerializer(serializers.ModelSerializer):
    legend = LegendSerializer(many=True)

    class Meta:
        model = Legends
        fields = '__all__'

class ClasificacionSerializer(serializers.ModelSerializer):
    table = TableSerializer(many=True)
    info = InfoSerializer()
    legends = LegendsSerializer(many=True)

    class Meta:
        model = Clasificacion
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','is_staff','date_joined']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'
