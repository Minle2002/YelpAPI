import requests

url = 'https://yelpapi-ahzs.onrender.com/search'

data = {
    "location": "E. Burnside Ave"
}

response = requests.post(url, json=data)

print(response.json())