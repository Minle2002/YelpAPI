import requests

url = 'http://127.0.0.1:5000/search'

data = {
    "limit": 1,
    "doctor_type": "dermatologist",
    "location": "New York"
}

response = requests.post(url, json=data)

print(response.json())