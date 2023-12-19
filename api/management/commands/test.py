import os
from django.utils import timezone
from api.models import RoundMatch
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        now = timezone.now()

        # Verificación y filtrado de partidos futuros
        next_matches = RoundMatch.objects.filter(schedule__gte=now).order_by('-schedule')
        next_matches_count = next_matches.count()
        print(f"Next matches count: {next_matches_count}")
        for match in next_matches:
            print(f'Next matches are {now.isoformat(), match.schedule.isoformat()}')

        # Revisión y filtrado de todos los partidos
        all_matches = RoundMatch.objects.all()
        all_matches_count = all_matches.count()
        print(f"All matches count: {all_matches_count}")
        for match in all_matches:
            time_difference = match.schedule - now
            print(f'All matches are {now.isoformat(), match.schedule.isoformat()}, Time difference: {time_difference}')
