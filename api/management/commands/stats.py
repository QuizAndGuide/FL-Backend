import requests
from django.core.management.base import BaseCommand
from api.serializers import StatsSerializer
from api.models import Stats
import json

class Command(BaseCommand):
    help = """Guarda las los 20 jugadores con mas goles, amarillas, rojas y asistencias en una tabla
            en vez de en 4 con el nombre de la lista en vez de total"""

    def handle(self, *args, **kwargs):
        url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&tz=Europe/Madrid&format=json&req=league_stats&league=1"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                with open('stats.json', 'w') as json_file:
                    json.dump(data, json_file)

                stats_lists = ['goals', 'yellow_cards', 'red_cards', 'asists']

                for stats_type in stats_lists:
                    stats_list = data['stats'][stats_type]

                    for stat_data in stats_list:
                        # Cambia 'total' por el nombre de la lista actual en el JSON si es necesario
                        stat_data[stats_type] = stat_data.pop('total', None)
                        player_id = stat_data.get('player_id')

                        existing_record = Stats.objects.filter(player_id=player_id)
                        
                        if existing_record:
                            existing_record.delete()
                            serializer = StatsSerializer(data=stat_data)
                            if serializer.is_valid():
                                serializer.save()
                                self.stdout.write(self.style.SUCCESS('Registro creado correctamente'))
                            else:
                                errors = serializer.errors
                                self.stderr.write(self.style.ERROR(f'Errores de validación para el registro: {errors}'))
                        else:
                            serializer = StatsSerializer(data=stat_data)
                            if serializer.is_valid():
                                serializer.save()
                                self.stdout.write(self.style.SUCCESS('Registro creado correctamente'))
                            else:
                                errors = serializer.errors
                                self.stderr.write(self.style.ERROR(f'Errores de validación para el registro: {errors}'))
            # Error handling for unsuccessful requests
            else:
                self.stderr.write(f'Error en la solicitud. Código de respuesta: {response.status_code}' if response.status_code != 200 else response.status_code)
        except Exception as e:
            # General error handling
            self.stderr.write(f'Error en la solicitud: {str(e)}')
