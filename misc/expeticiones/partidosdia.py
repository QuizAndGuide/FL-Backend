import requests

url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key={{APIKEY}}&format=json&req=matchsday"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
