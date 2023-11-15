from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('jornada', views.JornadaViewSet, basename='partidos')
router.register('stats', views.MaxGoalersViewSet, basename='goalers')


urlpatterns = router.urls
