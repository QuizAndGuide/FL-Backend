from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from datetime import datetime
from .models import UserProfile, Jornada
from .serializers import UserSerializer, UserProfileSerializer, JornadaSerializer
from rest_framework.exceptions import NotFound

class UserViewSet(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
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
    


class JornadaViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def partidos(self, request):
        proximos_partidos = Jornada.objects.filter(schedule__gte=datetime.now()).order_by('schedule')[:3]
        serializer = JornadaSerializer(proximos_partidos, many=True)        
        return Response(serializer.data)
