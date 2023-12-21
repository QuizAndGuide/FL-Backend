from celery import Celery, shared_task
from datetime import timedelta
from django.core.management import call_command
from django.utils import timezone
from .models import RoundMatch

app = Celery('football_quiz')

def update_command():
    # Llamar al comando "update" de forma síncrona
    call_command('update')

@shared_task
def process_matches():
    # Obtener el primer partido en el calendario
    first_match = RoundMatch.objects.filter(schedule__gte=timezone.now()).order_by('-schedule').first()

    if first_match:
        # Llamar al comando "update" de forma síncrona
        update_command()

        # Calcular la hora para la próxima ejecución, dos horas después del próximo partido
        next_execution_time = first_match.schedule + timedelta(hours=2)

        # Programar la próxima ejecución de la tarea
        schedule_next_task(next_execution_time)


def schedule_next_task(schedule_time):
    # Lógica para programar la tarea Celery dos horas después de la hora dada
    # Puedes usar la configuración de cron o el método crontab() de Celery aquí
    app.conf.beat_schedule['next_task'] = {
        'task': 'your_project.tasks.process_matches',
        'schedule': schedule_time,
    }
