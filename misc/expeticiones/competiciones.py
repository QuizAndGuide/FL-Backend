import requests

url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key={{APIKEY}}&tz=Europe/Madrid&req=categories&filter=my_leagues&format=json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
