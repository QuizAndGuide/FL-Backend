import requests

url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key={{APIKEY}}&tz=Europe/Madrid&format=json&req=competition_info&competitions=107"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
