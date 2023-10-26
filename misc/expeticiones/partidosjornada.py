import requests

url = "https://apiclient.besoccerapps.com/scripts/api/api.php?key=c6196c01e7c1d93932590f42beec9ef8&format=json&req=matchs&league=1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
