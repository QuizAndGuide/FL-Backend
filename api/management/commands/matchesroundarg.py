from datetime import datetime
import json
import requests
from django.core.management.base import BaseCommand
from api.models import RoundMatch
from api.serializers import RoundMatchSerializer

class Command(BaseCommand):
    help = 'obtiene la informacion de los partidos de la jornada en curso'

    def handle(self, *args, **kwargs):
        base_url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&format=json&req=matchs&league=1"
        url = base_url + f'&round={21}'


        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = json.loads(response.content)
                match = data.get('match', [])

                with open('round.json', 'w') as json_file:
                    json.dump(data, json_file)

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
                

                self.stdout.write("Datos de la jornada guardados o actualizados correctamente")
            # Error handling for unsuccessful requests
            else:
                self.stderr.write(f'Error en la solicitud. Código de respuesta: {response.status_code}')
        except requests.RequestException as e:
            # Manejar errores específicos de la solicitud
            self.stderr.write(f'Error en la solicitud: {str(e)}')
    