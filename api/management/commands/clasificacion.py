import requests
from django.core.management.base import BaseCommand
from api.serializers import ClasificacionSerializer
from api.models import Classification
import json

class Command(BaseCommand):
    help = 'debería guardar información simple de los jugadores de un equipo'

    def handle(self, *args, **kwargs):
        url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&format=json&req=tables&league=1"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                
                clas_data = data['table']
            
                for n in clas_data:
                    serializer = ClasificacionSerializer(data=n)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        # Registra errores en la consola
                        self.stderr.write(f'Error al guardar datos: {serializer.errors}')
            

           
        except Exception as e:
            self.stderr.write(f'Error en la solicitud: {str(e)}')
