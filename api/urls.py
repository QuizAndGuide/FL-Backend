from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet)
# router.register('jornada', views.JornadaViewSet, basename='partidos')
# router.register('stats', views.MaxGoalersViewSet, basename='goalers')

urlpatterns = [
    path('matches/', NextMatchesView.as_view(), name='partidos'),
    path('goalers/', MaxGoalersView.as_view(), name='scorers'),
]
urlpatterns += router.urls
