from models import RoundMatch 
from django.utils import timezone
from api.management.commands.update import Command as update_db

class AutoUpdater:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Código para ejecutar antes de que la vista sea llamada

        # Verifica si la solicitud se dirige a una vista específica
        if request.path == '/api/nextmatches/':
            # Realiza acciones adicionales para esta vista
            

            response = self.get_response(request)
            queryset = RoundMatch.objects.filter(schedule__lte=timezone.now()).order_by('schedule').first()
            return response
        elif queryset.result == 'x-x':
            update = update_db() 
            update.handle()           
