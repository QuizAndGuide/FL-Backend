import requests
from django.core.management.base import BaseCommand
from api.serializers import SimplePlayerSerializer 
from api.models import SimplePlayer
import json


class Command(BaseCommand):  # Esto es opcional, dependiendo de cómo ejecutes el script
    help = 'deberia guardar informacion simple de los jugadores de un eqipo'

    def handle(self, *args, **kwargs):
        team_id = input("team_id")

        url = f'https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&tz=Europe/Madrid&format=json&req=team&id={team_id}'  # Reemplaza con la URL real
        
        try:
            response = requests.get(url)

            if response.status_code == 200:
                json_data = response.json()
                if "team" in json_data:
                    team_data = json_data["team"]
                    if "squad" in team_data:
                        squad = team_data["squad"]
                        
                        for player_data in squad:
                            player_id = player_data.get('id') 
                            player_data['team_id'] = team_id              
                            for field in player_data:
                                if player_data.get(field) == '':
                                    player_data[field] = None
                                    
                            if player_id:
                                # Verifica si el jugador con el mismo 'id' ya existe en la base de datos
                                try:
                                    existing_player = SimplePlayer.objects.get(id=player_id)
                                except SimplePlayer.DoesNotExist:
                                    existing_player = None

                                if existing_player:
                                    # Si el jugador ya existe, actualiza los demás campos excepto 'id'
                                    for field, value in player_data.items():
                                        if field != 'id':
                                            setattr(existing_player, field, value)
                                    existing_player.save()
                                else:
                                    # Si el jugador no existe, crea un nuevo registro
                                    serializer = SimplePlayerSerializer(data=player_data)
                                    if serializer.is_valid():
                                        serializer.save()
                                    else:
                                        errors = serializer.errors
                                        print(f"Validation errors for player_data: {errors}")

            else:
                # Manejo de errores si la solicitud no fue exitosa
                self.stderr.write(f'Error en la solicitud. Código de respuesta: {response.status_code}')
        except Exception as e:
            # Manejo de errores generales
            self.stderr.write(f'Error en la solicitud: {str(e)}')
