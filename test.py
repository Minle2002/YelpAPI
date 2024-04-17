import requests

url = 'https://api.fda.gov/'

endpoint = 'drug/event.json'

data = {
    "search": "Ibuprofen"
}

response = requests.post(url + endpoint, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print('Error:', response.status_code)