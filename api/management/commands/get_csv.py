import csv
import requests
import json
from api.serializers import *
from django.core.management.base import BaseCommand 
from django.http import JsonResponse

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&format=json&req=tables&league=1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Utiliza el serializador para convertir los datos en un diccionario de Python
            serializer = ClasificacionSerializer(data=data)

            if serializer.is_valid():
                # Puedes acceder a los datos serializados con serializer.data
                serialized_data = serializer.data

                # Nombre del archivo CSV
                csv_filename = "datos.csv"

                # Abre el archivo CSV en modo escritura
                with open(csv_filename, 'w', newline='') as csvfile:
                    # Crea un escritor CSV
                    csv_writer = csv.DictWriter(csvfile, fieldnames=serialized_data.keys())

                    # Escribe la fila de encabezado con los nombres de las columnas
                    csv_writer.writeheader()

                    # Escribe los datos serializados como filas
                    csv_writer.writerow(serialized_data)

                # Puedes devolver una respuesta HTTP si lo deseas
                return JsonResponse({"message": "Datos guardados en el archivo CSV"}, status=200)
            else:
                # El serializer no es válido, maneja el error según tus necesidades
                return JsonResponse({"error": "No se pudo serializar correctamente"}, status=400)
        else:
            # La solicitud no fue exitosa, maneja el error según tus necesidades
            return JsonResponse({"error": "No se pudo obtener datos"}, status=response.status_code)
