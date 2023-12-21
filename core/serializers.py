from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from api.models import Profile

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', 'password', 'email']

    def validate_username(self, value):
        # Check if the username already exists
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists. Please choose a different one.")
        
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        
        return value

    def create(self, value):
        # Create the user and return it
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists. Please choose a different one.")
        
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        
        return True


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['username', 'email']