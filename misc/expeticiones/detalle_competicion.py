import requests

url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key={{APIKEY}}&tz=Europe/Madrid&format=json&req=data_competitions&competitions=1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
