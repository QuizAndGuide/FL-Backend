import requests
from django.core.management.base import BaseCommand
from api.serializers import SimplePlayerSerializer
from api.models import SimplePlayer
import json

class Command(BaseCommand):
    help = 'debería guardar información simple de los jugadores de un equipo'

def handle(self, *args, **kwargs):
    # team_id = input("team_id")
    
        
        url = f'https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&tz=Europe/Madrid&format=json&req=team&id={team_id}'

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

                            # Conditionally remove null fields
                            fields_to_remove = [field for field, value in player_data.items() if value is None]
                            for field in fields_to_remove:
                                del player_data[field]

                            # Check if the player with the same 'id' already exists in the database
                            try:
                                existing_player = SimplePlayer.objects.get(id=player_id)
                            except SimplePlayer.DoesNotExist:
                                existing_player = None

                            if existing_player:
                                # Update the player's information (except for 'id')
                                for field, value in player_data.items():
                                    if field != 'id':
                                        setattr(existing_player, field, value)
                                existing_player.save()
                            else:
                                # If the player doesn't exist, create a new record
                                serializer = SimplePlayerSerializer(data=player_data)
                                if serializer.is_valid():
                                    serializer.save()
                                else:
                                    errors = serializer.errors
                                    print(f"Validation errors for player_data: {errors}")

            else:
                # Error handling for unsuccessful requests
                self.stderr.write(f'Error en la solicitud. Código de respuesta: {response.status_code}')
        except Exception as e:
            # General error handling
            self.stderr.write(f'Error en la solicitud: {str(e)}')
