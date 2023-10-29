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
                
                clas_data = data['table']
                
                for n in clas_data:
                    dic = n | data['info']
                
                    
                    team_id = dic['id']

                        # Check if the team with the same 'id' already exists in the database
                    try:
                        existing_team = Clasificacion.objects.get(id=team_id)
                    except Clasificacion.DoesNotExist:
                        existing_team = None

                    if existing_team:
                        # Update the team's information (except for 'id')
                        for field, value in dic.items():
                            if field != 'id':
                                setattr(existing_team, field, value)
                        existing_team.save()
                    else:
                        # If the team doesn't exist, create a new record
                        serializer = ClasificacionSerializer(data=dic)
                        if serializer.is_valid():
                            serializer.save()
                        else:
                            errors = serializer.errors
                            print(f"Validation errors for team: {errors}")

            # Error handling for unsuccessful requests
            self.stderr.write(f'Error en la solicitud. Código de respuesta: {response.status_code}')
        except Exception as e:
            # General error handling
            self.stderr.write(f'Error en la solicitud: {str(e)}')
