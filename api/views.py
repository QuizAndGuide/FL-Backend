from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, permission_classes
from django.utils import timezone
from .models import Profile, RoundMatch, Stats
from .serializers import ProfileSerializer, RoundMatchSerializer, StatsSerializer
from .permissions import *
from rest_framework.exceptions import NotFound


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, permission_classes=[ViewCustomerHistoryPermission])
    def history(self, request, pk):
        return Response('ok')

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = Profile.objects.get(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = ProfileSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProfileSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)



@permission_classes([IsAuthenticated])
class NextMatchesView(APIView):
    def get(self, request, format=None):
        next_matches = RoundMatch.objects.filter(schedule__gte=timezone.now()).order_by(-'schedule')

        serializer = RoundMatchSerializer(next_matches, many=True)        
        return Response(serializer.data)
    
    
@permission_classes([IsAuthenticated])
class LastMatchesView(APIView):
    def get(self, request, format=None):
        last_matches = RoundMatch.objects.filter(status=1).order_by('-schedule')
        print(last_matches)
        serializer = RoundMatchSerializer(last_matches, many=True)        
        return Response(serializer.data)
    
    
@permission_classes([IsAuthenticated])
class MaxGoalersView(APIView):
    def get(self, request, format=None):
        max_goalers = Stats.objects.all().order_by('-goals')
        serializer = StatsSerializer(max_goalers, many=True)
        return Response(serializer.data)
    
# class JornadaViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]

#     @action(detail=False, methods=['get'])
#     def matches(self, request):
#         proximos_partidos = Jornada.objects.filter(schedule__gte=datetime.now()).order_by('schedule')[:3]
#         serializer = MatchesSerializer(proximos_partidos, many=True)        
#         return Response(serializer.data)


# class MaxGoalersViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]

#     @action(detail=False, methods=['get'])
#     def max_goalers(self, request):
#         max_goalers = Stats.objects.all().order_by('-goals')[:3]
#         serializer = MaxGoalersSerializer(max_goalers, many=True)
        
#         return Response(serializer.data)