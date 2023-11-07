import requests
from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):
    help = 'Save simple player information for teams as JSON files'

    def handle(self, *args, **kwargs):
        team_ids = [2107, 429, 1236, 369, 2120, 347, 486, 2080, 1887, 2647, 1217, 603, 2716, 2563, 1102, 1623, 137, 712, 4235, 183]

        for team_id in team_ids:
            url = f'https://apiclient.besoccerapps.com/scripts/api/api.php?key=5377a0809e482cab755825001d412121&tz=Europe/Madrid&format=json&req=team&id={team_id}'

            try:
                response = requests.get(url)

                if response.status_code == 200:
                    json_data = response.json()
                    basealias = json_data.get('team', {}).get('basealias', f'team_{team_id}')

                    filename = f'{basealias}.json'

                    with open(filename, 'w') as file:
                        json.dump(json_data, file)  # Serialize JSON data

                    print(f'Data for team {team_id} saved to {filename}')
                else:
                    print(f'Failed to retrieve data for team {team_id}')
            except requests.RequestException as e:
                print(f'An error occurred while fetching data for team {team_id}: {str(e)}')
