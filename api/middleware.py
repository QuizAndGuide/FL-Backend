from models import RoundMatch 
from django.utils import timezone
from api.management.commands.update import Command as update_db

class AutoUpdater:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def update_db(self):
        ending_game = timezone.now() + timezone.timedelta(hours=2, minutes=15)
        queryset = RoundMatch.objects.filter(schedule__lte=ending_game).order_by('schedule').first()
        if queryset.result == 'x-x':
            update = update_db() 
            update.handle()

    def __call__(self, request):

        if request.path == '/api/nextmatches/':
            response = self.get_response(request)
            update_db.delay(2)
            
            return response
             
# viendo si implementar la llamada del comando update como middleware o en celery, o ambos

# todavia dandole vueltas a la logica para ver si esta desactualizada la base de datos

