from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework import status
from core.models import User
from .models import UserProfile, Player, Teams, Classification, SimplePlayer
from .serializers import UserSerializer, UserProfileSerializer, PlayerSerializer, ClasificacionSerializer, TeamsSerializer, SimplePlayerSerializer
import logging


class PlayerIdViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'team_id' 

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'team_id' in self.kwargs:
            queryset = queryset.filter(team_id=self.kwargs['team_id'])
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    
class PlayerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = { 'id_team': self.kwargs['id_team'], 'id_player': self.kwargs['id_player'] }
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj
    def list(self, request, id_team=None):
        queryset = self.queryset.filter(id_team=id_team)
        serializer = PlayerSerializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def put(self, request, *args, **kwargs):
        try:
            player = self.get_object()
            serializer = PlayerSerializer(player, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs.get('username', None)
        if username is not None:
            return UserProfile.objects.filter(username=username)
        else:
            raise NotFound("El parámetro 'username' es requerido")

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

    
class UserProfileDeleteView(generics.DestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'

class TeamsRetrieveUpdateDestroyCreateView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    serializer_class = TeamsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'name_show'
    lookup_url_kwarg = 'name_show'

    def get_queryset(self):
        return Teams.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj  

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
    
def authenticate(email=None, password=None):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(email=email)
    except UserModel.DoesNotExist:
        return None

    if user.check_password(password):
        return user

# En tu LoginView
class LoginViewSet(APIView):
    def post(self, request, format=None):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response(status=401)
        
class ClassificationListCreateView(generics.ListCreateAPIView):
    serializer_class = ClasificacionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        year = self.kwargs['year']
        round = self.kwargs['round']
        return Classification.objects.filter(year=year, round=round)

    def put(self, request, *args, **kwargs):
        year = self.kwargs['year']
        round = self.kwargs['round']
        queryset = Classification.objects.filter(year=year, round=round)
        data = request.data  # This should be a list of teams
        if isinstance(data, list):  # Check if data is a list
            # Update each team
            for team_data in data:
                team = queryset.get(id=team_data['id'])
                serializer = ClasificacionSerializer(team, data=team_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Expected a list of teams"}, status=status.HTTP_400_BAD_REQUEST)

class SimplePlayerList(generics.ListCreateAPIView):
    queryset = SimplePlayer.objects.all()
    serializer_class = SimplePlayerSerializer