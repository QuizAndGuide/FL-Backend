import os
from dotenv import load_dotenv
from django import setup as django_setup
from django.utils import timezone
from api.models import RoundMatch

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Configura la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("DJANGO_SETTINGS_MODULE"))

# Configura las configuraciones de Django
django_setup()

# Ahora puedes acceder a las configuraciones de Django
from django.conf import settings

# Tu código restante
next_matches = RoundMatch.objects.filter(schedule__gte=timezone.now()).order_by('-schedule')
print(timezone.now(), next_matches)
