# import requests
# from api.serializers import *
# from django.core.management.base import BaseCommand 
# from django.http import JsonResponse

# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key={{APIKEY}}&format=json&req=tables&league=1"
#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()

#             # Utiliza el serializador para crear una instancia de MiModelo
#             serializer = MiModeloSerializer(data=data)

#             if serializer.is_valid():
#                 # Guarda la instancia en la base de datos
#                 serializer.save()

#                 # Puedes devolver la instancia serializada como respuesta HTTP si lo deseas
#                 return JsonResponse(serializer.data, safe=False)
#             else:
#                 # El serializer no es válido, maneja el error según tus necesidades
#                 return JsonResponse({"error": "No se pudo serializar correctamente"}, status=400)
#         else:
#             # La solicitud no fue exitosa, maneja el error según tus necesidades
#             return JsonResponse({"error": "No se pudo obtener datos"}, status=response.status_code)


