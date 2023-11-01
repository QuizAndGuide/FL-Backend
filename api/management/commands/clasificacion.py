import requests
from django.core.management.base import BaseCommand
from api.serializers import ClasificacionSerializer
from api.models import Clasificacion
import json

class Command(BaseCommand):
    help = 'debería guardar información simple de los jugadores de un equipo'

    def handle(self, *args, **kwargs):
        url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&format=json&req=tables&league=1"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                serializer = ClasificacionSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    errors = serializer.errors
                    print(f"Validation errors for team: {errors}")
                    
                # serializer = Clasificacion(data)
                
                # serializer.save() 
                
                # # clasificacion_data = {
                # #     "table": data.get("table", []),
                # #     "info": data.get("info", {}),
                # #     "legends": data.get("legends", []),
                # # }
                
                # # # Guarda los datos en el modelo Clasificacion
                # # clasificacion = Clasificacion(**clasificacion_data)
                # # clasificacion.save()
                
                self.stdout.write("Datos de clasificación guardados correctamente.")
            # Error handling for unsuccessful requests
            else:
                self.stderr.write(f'Error en la solicitud. Código de respuesta: {response.status_code}'if response.status_code != 200 else response.status_code)
        except Exception as e:
            # General error handling
            self.stderr.write(f'Error en la solicitud: {str(e)}')
