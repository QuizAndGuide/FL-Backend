import requests
from django.core.management.base import BaseCommand
from api.serializers import ClasificacionSerializer, TableSerializer, LegendsSerializer, LegendSerializer
from api.models import Clasificacion, Legend, Legends, Table 
import json

class Command(BaseCommand):
    help = 'debería guardar información simple de los jugadores de un equipo'

    def handle(self, *args, **kwargs):
        url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&format=json&req=tables&league=1"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                table = data['table']

                # Verificar si la lista 'table' no está vacía
                if table:
                    first_item = table[0]
                    round_value = first_item.get('round')

                    # Buscar el registro existente en función del campo 'round'
                    existing_record = Table.objects.filter(round=round_value).first()

                    # Serializar y guardar todos los elementos de la lista 'table'
                    for item in table:
                        serializer = TableSerializer(existing_record, data=item)
                        if serializer.is_valid():
                            serializer.save()
                            self.stdout.write("Registro actualizado o creado correctamente.")
                        else:
                            errors = serializer.errors
                            self.stderr.write(f"Errores de validación para el registro: {errors}")
                    
                # data = response.json()
                # serializer = ClasificacionSerializer(data=data)
                # serializer.is_valid()
                # serializer.save()
                    
                # # serializer = Clasificacion(data)
                
                # # serializer.save() 
                
                # clasificacion_data = {
                #     "table": data.get("table", []),
                #     "info": data.get("info", {}),
                #     "legends": data.get("legends", []),
                # }
                
                # Guarda los datos en el modelo Clasificacion
                # clasificacion = Clasificacion(**clasificacion_data)
                # clasificacion.save()
                
                self.stdout.write("Datos de clasificación guardados correctamente.")
            # Error handling for unsuccessful requests
            else:
                self.stderr.write(f'Error en la solicitud. Código de respuesta: {response.status_code}'if response.status_code != 200 else response.status_code)
        except Exception as e:
            # General error handling
            self.stderr.write(f'Error en la solicitud: {str(e)}')
