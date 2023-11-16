import requests
from django.core.management.base import BaseCommand
from api.serializers import RoundSerializer
from api.models import Round
import json
from datetime import datetime, date

class Command(BaseCommand):
    help = 'Partidos de la jornada actual y si quedan menos de 3 de la siguiente tambien'

    def handle(self, *args, **kwargs):
        url_base = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&format=json&req=matchs&league=1"
        round_increment = 1

        try:
            response = requests.get(url_base)

            if response.status_code == 200:
                data = response.json()
                match_list = data.get('match')

                # Verificar si la lista 'match' no está vacía
                if match_list:
                    future_dates_count = 0

                    # Serializar y guardar todos los elementos de la lista 'match'
                    for item in match_list:
                        round_value = item.get('round')
                        existing_record = Round.objects.filter(round=round_value).first()
                        item['date'] = datetime.strptime(item['date'], '%Y/%m/%d').date()
                        # Verificar si la fecha es futura
                        match_date_str = item.get('schedule')
                        match_date = datetime.strptime(match_date_str, "%Y-%m-%d %H:%M:%S")
                        if match_date > datetime.now():
                            future_dates_count += 1

                        # Serializar y guardar los datos del elemento actual
                        serializer = RoundSerializer(existing_record, data=item)
                        if serializer.is_valid():
                            serializer.save()
                            self.stdout.write("Record updated or created successfully.")
                        else:
                            errors = serializer.errors
                            self.stderr.write(f"Validation errors for the record: {errors}")

                    # Check if there are more than three elements with future dates
                    if future_dates_count <= 3:
                        # Incrementar el valor de 'round' para la nueva solicitud
                        new_round = round_value + round_increment
                        new_url = f"{url_base}&round={new_round}"

                        # Realizar una nueva solicitud con 'round' incrementado
                        new_response = requests.get(new_url)

                        if new_response.status_code == 200:
                            new_data = new_response.json()
                            new_match_list = new_data.get('match')

                            # Serializar y guardar los datos de la nueva solicitud
                            for new_item in new_match_list:
                                serializer = RoundSerializer(existing_record, data=new_item)
                                if serializer.is_valid():
                                    serializer.save()
                                    self.stdout.write("Record updated or created successfully.")
                                else:
                                    errors = serializer.errors
                                    self.stderr.write(f"Validation errors for the record: {errors}")

                    self.stdout.write("Match data saved successfully.")
            else:
                self.stderr.write(f'Error in the request. Response code: {response.status_code}' if response.status_code != 200 else response.status_code)
        except Exception as e:
            self.stderr.write(f'Error in the request: {str(e)}')




import requests
from django.core.management.base import BaseCommand
from api.serializers import RoundSerializer
from api.models import Round
import json

class Command(BaseCommand):
    help = 'Should save simple information of team players'

    def handle(self, *args, **kwargs):
        url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&format=json&req=matchs&league=1"
        ronda = ()
        
        def response(url, ronda):
            if ronda:
                url = url + f"&round={ronda}"  
                try:
                    response = requests.get(url)

                    if response.status_code == 200:
                        data = response.json()
                        match_list = data.get('match')
                        print(match_list)
                        # Verificar si la lista 'match' no está vacía
                        if match_list:
                            round = match_list[0].get('round')  # Assuming the list is not empty

                            # Serializar y guardar todos los elementos de la lista 'match'
                            for item in match_list:
                                item['match_id'] = item.pop('id')
                                item['date'] = datetime.strptime(item['date'], '%Y/%m/%d').date()
                                existing_record = Round.objects.filter(round=round).first()

                                # Serializar y guardar los datos del elemento actual
                                serializer = RoundSerializer(existing_record, data=item)
                                if serializer.is_valid():
                                    serializer.save()
                                    self.stdout.write("Record updated or created successfully.")
                                else:
                                    errors = serializer.errors
                                    self.stderr.write(f"Validation errors for the record: {errors}")

                            # Incrementar el valor de 'round' para la nueva solicitud
                            ronda = int(round) + 1
                            print(round)
                            
                            self.stdout.write("Match data saved successfully.")
                    else:
                        self.stderr.write(f'Error in the request. Response code: {response.status_code}' if response.status_code != 200 else response.status_code)
                except Exception as e:
                    self.stderr.write(f'Error in the request: {str(e)}')
                    return ronda
        
        
        response(url, ())
        response(url, ronda)
        