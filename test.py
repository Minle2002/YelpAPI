import requests

url = 'http://127.0.0.1:5000/search'

data = {
    "location": "new york city",
    "limit": 10,  # Specify the number of results you want
    "doctor_type": "doctors"  # Specify the type of doctor you're searching for
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print('Error:', response.status_code)