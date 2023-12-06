from datetime import datetime
import json
import requests
from django.core.management.base import BaseCommand
from api.models import RoundMatch
from api.serializers import RoundMatchSerializer, StatsSerializer

class Command(BaseCommand):
    help = 'obtiene la informacion de los partidos de la jornada en curso'

    def handle(self, *args, **kwargs):
        url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&format=json&req=matchs&league=1"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = json.loads(response.content)
                match = data.get('match', [])

                # with open('round.json', 'w') as json_file:
                #     json.dump(data, json_file)

                # Verificar si la lista 'table' no está vacía
                if match[0]:

                    for item in match:
                        id = item.get('id')
                        round = item.get('round')
                        existing_record = RoundMatch.objects.filter(pk=id)
                        if existing_record:
                            existing_record.delete()
                            serializer = RoundMatchSerializer(data=item)
                            if serializer.is_valid():
                                serializer.save()
                                self.stdout.write("Registro actualizado.")
                            else:
                                errors = serializer.errors
                                self.stderr.write(f"Errores de validación para el registro: {errors}")
                        else:
                            serializer = RoundMatchSerializer(data=item)
                            if serializer.is_valid():
                                serializer.save()
                                self.stdout.write("Registro actualizado.")
                            else:
                                errors = serializer.errors
                                self.stderr.write(f"Errores de validación para el registro: {errors}")
            next_round =+ int(round)  
            next_round_url = url + f'&round={next_round}'
            response = requests.get(next_round_url)

            if response.status_code == 200:
                data = json.loads(response.content)
                match = data.get('match', [])

                # with open('round.json', 'w') as json_file:
                #     json.dump(data, json_file)

                # Verificar si la lista 'table' no está vacía
                if match[0]:

                    for item in match:
                        id = item.get('id')
                        existing_record = RoundMatch.objects.filter(pk=id)
                        if existing_record:
                            existing_record.delete()
                            serializer = RoundMatchSerializer(data=item)
                            if serializer.is_valid():
                                serializer.save()
                                self.stdout.write("Next_round: Registro actualizado.")
                            else:
                                errors = serializer.errors
                                self.stderr.write(f"Next_round: Errores de validación para el registro: {errors}")
                        else:
                            serializer = RoundMatchSerializer(data=item)
                            if serializer.is_valid():
                                serializer.save()
                                self.stdout.write("Next_round: Registro actualizado.")
                            else:
                                errors = serializer.errors
                                self.stderr.write(f"Next_round: Errores de validación para el registro: {errors}")
            
                stats_url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&tz=Europe/Madrid&format=json&req=league_stats&league=1"

                response = requests.get(stats_url)

                if response.status_code == 200:
                    data = response.json()

                    # with open('stats.json', 'w') as json_file:
                    #     json.dump(data, json_file)

                    stats_lists = ['goals', 'yellow_cards', 'red_cards', 'asists']

                    for stats_type in stats_lists:
                        stats_list = data['stats'][stats_type]

                        for stat_data in stats_list:
                            # Cambia 'total' por el nombre de la lista actual en el JSON si es necesario
                            stat_data[stats_type] = stat_data.pop('total', None)

                            # Serializar y guardar en la base de datos
                            serializer = StatsSerializer(data=stat_data)
                            if serializer.is_valid():
                                serializer.save()
                                self.stdout.write(self.style.SUCCESS('Stats: Registro creado correctamente'))
                            else:
                                errors = serializer.errors
                                self.stderr.write(self.style.ERROR(f'Stats: Errores de validación para el registro: {errors}'))

                        self.stdout.write("Datos de la jornada guardados o actualizados correctamente")
            # Error handling for unsuccessful requests
            else:
                self.stderr.write(f'Error en la solicitud. Código de respuesta: {response.status_code}')
        except requests.RequestException as e:
            # Manejar errores específicos de la solicitud
            self.stderr.write(f'Error en la solicitud: {str(e)}')
    