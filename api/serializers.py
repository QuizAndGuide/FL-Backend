from typing import Any
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Classification, Teams, Player, SimplePlayer

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        

class SimplePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimplePlayer
        fields = '__all__'
    


class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
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
