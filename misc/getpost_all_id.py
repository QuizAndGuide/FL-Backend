# from django.http import JsonResponse
# from django.core.management.base import BaseCommand 
# from api.models import *  # Reemplaza "TuModelo" con el nombre de tu modelo
# import requests
# import json

# class Command(BaseCommand):  # Esto es opcional, dependiendo de cómo ejecutes el script
#     def handle(self, *args, **kwargs):  # Esto es opcional, dependiendo de cómo ejecutes el script
#         url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key={{APIKEY}}&format=json&req=tables&league=1"
#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()
            
#             # Crea una instancia de tu modelo y guarda los datos en la base de datos
#             datos_api = DatosAPI(
#                 campo1=data['campo1'],  # Ajusta los campos según los datos de la API
#                 campo2=data['campo2'],
#                 # Completa los otros campos según tus necesidades
#             )
#             datos_api.save()  # Guarda la instancia en la base de datos


# def api_request_and_serialize(request):
#     # Obtén todas las instancias de TuModelo o filtra según tus necesidades
#     objetos = Teams.objects.all()  # Puedes aplicar filtros según tus necesidades

#     data_list = []  # Aquí almacenaremos los datos serializados

#     for objeto in objetos:
#         # Construye la URL de la API utilizando la ID u otros campos de tu modelo     ##jugadoressss
#         url = f"http://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&tz=Europe/Madrid&format=json&req=player&id={objeto.id}"
        
#         # Realiza la solicitud a la API
#         response = requests.get(url)

#         if response.status_code == 200:
#             # La solicitud fue exitosa, ahora puedes trabajar con los datos de respuesta
#             data = response.json()  # Convierte la respuesta JSON en un diccionario de Python
#             data_list.append(data)  # Agrega los datos a la lista

#     # Serializa la lista de datos recopilados
#     serialized_data = json.dumps(data_list)

#     # Puedes devolver los datos serializados como respuesta HTTP si lo deseas
#     return JsonResponse(serialized_data, safe=False)


# def api_request_and_save(request):
#     objetos = TuModelo.objects.all()
#     data_list = []

#     for objeto in objetos:
#         url = f"https://apiclient.besoccerapps.com/scripts/api/api.php?key={{APIKEY}}&format=json&req=tables&league={objeto.id}"
#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()
            
#             # Crea una instancia de tu modelo y guarda los datos en la base de datos
#             datos_api = DatosAPI(
#                 campo1=data['campo1'],  # Ajusta los campos según los datos de la API
#                 campo2=data['campo2'],
#                 # Completa los otros campos según tus necesidades
#             )
#             datos_api.save()  # Guarda la instancia en la base de datos

#             data_list.append(data)

#     # Serializa la lista de datos recopilados (si es necesario)
#     serialized_data = json.dumps(data_list)

#     return JsonResponse(serialized_data, safe=False)
