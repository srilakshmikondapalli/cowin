import requests

url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"

payload={}
headers = {
  'Accept': 'application/json',
  'Accept-Language': 'hi_IN'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())