from .views import UserViewSet, UserProfileUpdateView, UserProfileDeleteView, CurrentUserView, LoginViewSet, ClassificationListCreateView, TeamsRetrieveUpdateDestroyCreateView, PlayerViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('login/', LoginViewSet.as_view(), name='login'),
    path('users/', UserViewSet.as_view(), name='users'),
    path('@/<str:username>/', UserProfileUpdateView.as_view(), name='userprofile_update'),
    path('@/<str:username>/delete', UserProfileDeleteView.as_view(), name='userprofile_delete'),
    path('current-user-profile/', CurrentUserView.as_view(), name='user-profile-present'),
    path('spain/first-division/classification/<int:year>/<int:round>/', ClassificationListCreateView.as_view(), name='classification_list_create'),
    path('spain/first-division/2023-2024/teams/<str:name_show>/', TeamsRetrieveUpdateDestroyCreateView.as_view(), name='teams_update'),
    path('spain/first-division/2023-2024/teams/<str:id_team>/<str:id_player>/', PlayerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'post': 'create'}), name='player_detail'),
]

