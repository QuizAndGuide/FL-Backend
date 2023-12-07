from django.core.management.base import BaseCommand
from api.management.commands.matchesroundandnext import Command as MatchesRoundAndNextCommand
from api.management.commands.stats import Command as StatsCommand

class Command(BaseCommand):
    help = 'Comando combinado que ejecuta varios comandos personalizados.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando el comando combinado...'))

        # Acción 1: Ejecutar Comando1
        self.stdout.write(self.style.SUCCESS('Ejecutando matchesroundandnext...'))
        comando1 = MatchesRoundAndNextCommand()
        comando1.handle()

        # Acción 2: Ejecutar Comando2
        self.stdout.write(self.style.SUCCESS('Ejecutando stats...'))
        comando2 = StatsCommand()
        comando2.handle()


        self.stdout.write(self.style.SUCCESS('Comando combinado completado.'))