from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

YELP_API_KEY = '-QtUYJLkBVr7lUpx3i2WsKCz2ccD9OB2lohynohLW6z2P07yWzlRJqU-5dxtJ0l2GgojI1YLkMeSqRquysFgVftyLEiSkyobBNJ_E3cQA-RDiKSN880jy1kBnU40ZnYx'

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()

    limit = data.get('limit')
    doctor_type = data.get('doctor_type', 'doctors')
    location = data['location']
    
    headers = {'Authorization': f'Bearer {YELP_API_KEY}'}
    params = {'term': doctor_type,
              'location': location,
              'limit': limit,
              'sort_by': 'rating'
    }
    
    try:
        response = requests.get('https://api.yelp.com/v3/businesses/search', headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        businesses = data.get('businesses', [])
        

        simplified_businesses = []
        for business in businesses:
            categories = [category['title'] for category in business.get('categories', [])]
            simplified_business = {
                'name': business['name'],
                'address': ', '.join(business['location']['display_address']),
                'phone': business.get('phone', 'N/A'),
                'email': business.get('email', 'N/A'),
                'specialty': ', '.join(categories) if categories else 'N/A'
            }
            simplified_businesses.append(simplified_business)

        return jsonify({'businesses': simplified_businesses, 'location': location})
    except requests.RequestException as e:
        return jsonify({'error': f'Failed to retrieve data from Yelp API: {str(e)}'}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)