import requests

url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key={{APIKEY}}&format=json&req=tables&league=1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
