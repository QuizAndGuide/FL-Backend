from celery import Celery, shared_task
from celery.schedules import crontab
from datetime import timedelta
from django.core.management import call_command
from django.utils import timezone
from .models import RoundMatch

@shared_task
def update_command():
    # Llamar al comando "update" de forma síncrona
    call_command('update')

@shared_task
def process_matches():
    # Obtener los partidos cuya programación está en el futuro
    future_matches = RoundMatch.objects.filter(schedule__gte=timezone.now())

    for match in future_matches:
        # Calcular la hora para ejecutar el comando "update", dos horas y media después de cada programación
        execution_time = match.schedule + timedelta(hours=2, minutes=30)

        # Programar la ejecución del comando "update"
        update_command.apply_async(eta=execution_time)
