from models import RoundMatch 
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
            update_db.delay(2)
            
            return response
             
# viendo si implementar la llamada del comando update como middleware o en celery, o ambos