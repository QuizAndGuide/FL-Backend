from .models import RoundMatch 
from django.utils import timezone
from api.management.commands.update import Command as update_db

class AutoUpdater:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def update_db(self):
        queryset = RoundMatch.objects.filter(schedule__lte=timezone.now()).order_by('schedule').first()
        if queryset.result == 'x-x':
            update = update_db() 
            update.handle()

    def __call__(self, request):

        if request.path == '/api/nextmatches/':
            response = self.get_response(request)
            
            return response
             

# viendo si implementar la llamada del comando update como middleware o en celery, o ambos

# todavia dandole vueltas a la logica para ver si esta desactualizada la base de datos

from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated

class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if (
            response.status_code == 401
            and "Authentication credentials were not provided." in response.data.get("detail", "")
        ):
            # Almacenar la URL original antes de redirigir
            request.session['original_path'] = request.path
            # Redirigir a auth/jwt/create si las credenciales no fueron proporcionadas
            return redirect('/auth/jwt/create')

        return response

>>>>>>> Stashed changes
