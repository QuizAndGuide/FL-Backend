from django.views.generic import TemplateView 
from .views import CreateUserAPIView
from django.urls import path

# URLConf
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html')),
    path('create_user/', CreateUserAPIView.as_view(), name='create_user'),

]