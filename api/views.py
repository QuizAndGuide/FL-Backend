from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from datetime import datetime
from .models import User, UserProfile, Jornada
from .serializers import UserSerializer, UserProfileSerializer, JornadaSerializer
from rest_framework.exceptions import NotFound

class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'

    def get_queryset(self):
        username = self.kwargs.get('username')
        if username is not None:
            return UserProfile.objects.filter(username=username)
        else:
            raise NotFound("El parámetro 'username' es requerido")

class LoginViewSet(APIView):
    def post(self, request, format=None):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


class JornadaViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def list_proximos_partidos(self, request):
        proximas_entradas = Jornada.objects.filter(schedule__gte=datetime.now()).order_by('schedule')[:3]        
        serializer = JornadaSerializer(proximas_entradas, many=True)        
        return Response(serializer.data)
