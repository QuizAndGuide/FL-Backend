from celery import shared_task
from django.core.management import call_command

@shared_task
def ejecutar_update():
    call_command('update')  # Reemplaza 'ejemplo' con el nombre de tu comando