import requests
from django.core.management.base import BaseCommand
from api.serializers import MonthMatchesinputSerializer, MonthMatchesUpdateSerializer
from api.models import Round
from datetime import datetime
import json

class Command(BaseCommand):
    help = 'debería guardar información simple de los jugadores de un equipo'

    def handle(self, *args, **kwargs):

        # Obtener la fecha actual
        now = datetime.now()

        # Obtener el mes y el año por separado
        month = now.month
        year = now.year
        url = f'https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&format=json&req=matchs_month&category=1&extra={month}&year={year}'
        

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                
                with open('MonthMatches.json', 'w') as json_file:
                    json.dump(data, json_file)

                matches_list = [match for week in data["d"] for match in week.get("matches", [])]
                if matches_list:
                    for item in matches_list:
                        id = item.get('id')
                        existing_record = Round.objects.filter(id=id)
                            # Cambia esta línea para mantener 'date' como 'date' en lugar de convertirlo a 'datetime'
                        # item['date'] = datetime.strptime(item['date'], '%Y/%m/%d').date()
                        if existing_record:
                            # Serializar y guardar o actualizar todos los elementos de la lista 'table'
                            serializer = MonthMatchesUpdateSerializer(existing_record, data=item)
                            if serializer.is_valid():
                                serializer.save()
                                self.stdout.write("Registro actualizado.")
                            else:
                                errors = serializer.errors
                                self.stderr.write(f"Errores de validación para el registro: {errors}")
                        else:
                                serializer = MonthMatchesinputSerializer(data=item)
                                if serializer.is_valid():
                                    serializer.save()
                                    self.stdout.write("Registro creado correctamente.")
                
                self.stdout.write("Datos de clasificación guardados correctamente.")
            # Error handling for unsuccessful requests
            else:
                self.stderr.write(f'Error en la solicitud. Código de respuesta: {response.status_code}'if response.status_code != 200 else response.status_code)
        except Exception as e:
            # General error handling
            self.stderr.write(f'Error en la solicitud: {str(e)}')
