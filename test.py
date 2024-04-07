import requests

# Replace this with the URL of your Flask application
url = 'http://127.0.0.1:5000/search'

data = {
    "location": "New York"
}

response = requests.post(url, json=data)

print(response.json())