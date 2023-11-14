import requests
from django.core.management.base import BaseCommand
from api.serializers import JornadaSerializer
from api.models import Jornada
import json

class Command(BaseCommand):
    help = 'debería guardar información simple de los jugadores de un equipo'

    def handle(self, *args, **kwargs):
        url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&format=json&req=matchs_month&category=1&extra=3"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                table = data['match']
                
                with open('partidosmes.json', 'w') as json_file:
                    json.dump(data, json_file)

            
                self.stdout.write("Datos de clasificación guardados correctamente.")
            # Error handling for unsuccessful requests
            else:
                self.stderr.write(f'Error en la solicitud. Código de respuesta: {response.status_code}'if response.status_code != 200 else response.status_code)
        except Exception as e:
            # General error handling
            self.stderr.write(f'Error en la solicitud: {str(e)}')
