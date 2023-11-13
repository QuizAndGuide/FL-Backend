from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginViewSet, JornadaViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'proximos_partidos', JornadaViewSet, basename='proximos_partidos')

urlpatterns = [
    path('login/', LoginViewSet.as_view(), name='login'),
    path('', include(router.urls)),
]