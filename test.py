import requests

url = 'http://127.0.0.1:5000/search'

data = {
    "location": "New York",
    "doctor_type": "dermatologist"
}

response = requests.post(url, json=data)

print(response.json())