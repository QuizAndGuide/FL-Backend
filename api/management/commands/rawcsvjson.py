from django.core.management.base import BaseCommand
import requests
import csv
import json

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&format=json&req=tables&league=1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file)

            with open('data.csv', 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                header = data['table'][0].keys()
                writer.writerow(header)
                for row in data['table']:
                    writer.writerow(row.values())

        else:
            print("No se pudo obtener datos de la API")
