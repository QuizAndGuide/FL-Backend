import requests
from django.core.management.base import BaseCommand
from api.serializers import SimplePlayerSerializer 
import json


class Command(BaseCommand):  # Esto es opcional, dependiendo de cómo ejecutes el script
    help = 'deberia guardar informacion simple de los jugadores de un eqipo'

    def handle(self, *args, **kwargs):
        team_id = input("team_id")

        url = f'https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&tz=Europe/Madrid&format=json&req=team&id={team_id}'  # Reemplaza con la URL real
        
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                print(data)
                with open('Detalleequipo.json', 'r') as file:
                    json_data = json.load(file)
                    if "team" in data:
                        team_data = data["team"]
                        if "squad" in team_data:
                            squad = team_data["squad"]


                
                
                
                for player_data in squad:
                    serializer = SimplePlayerSerializer(data=player_data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        # Handle validation errors for individual players as needed
                        errors = serializer.errors
                
                else:
                    # Manejo de errores si el serializador no es válido
                    self.stderr.write('El serializador no es válido.')
            else:
                # Manejo de errores si la solicitud no fue exitosa
                self.stderr.write(f'Error en la solicitud. Código de respuesta: {response.status_code}')
        except Exception as e:
            # Manejo de errores generales
            self.stderr.write(f'Error en la solicitud: {str(e)}')

            
            
# import json

# # Abre el archivo JSON en modo lectura
# with open('datos.json', 'r') as archivo:
#     # Carga el contenido del archivo en una variable como un diccionario
#     datos = json.load(archivo)
#     squad_json = datos["team"]["squad"]