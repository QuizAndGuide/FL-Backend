from datetime import datetime
import requests
from django.core.management.base import BaseCommand
from api.serializers import AgendaSerializer
from api.models import Agenda
import json

class Command(BaseCommand):
    help = 'debería guardar información simple de los jugadores de un equipo'

    def handle(self, *args, **kwargs):
        url = f"http://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&format=json&req=agenda&page=1&tz=Europe/Madrid&competitions=1&lang=es"


        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                
                with open('agenda.json', 'w') as json_file:
                    json.dump(data, json_file)

                # Verificar si la lista 'table' no está vacía
                    serializer = AgendaSerializer(data=data)
                    serializer.is_valid()
                    serializer.save()
                    self.stdout.write("Registro actualizado o creado correctamente.")
                     
              
                
                self.stdout.write("Datos de la jornada guardados correctamente")
            # Error handling for unsuccessful requests
            else:
                self.stderr.write(f'Error en la solicitud. Código de respuesta: {response.status_code}'if response.status_code != 200 else response.status_code)
        except Exception as e:
            # General error handling
            self.stderr.write(f'Error en la solicitud: {str(e)}')
