from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

YELP_API_KEY = '-6OSNIwtvbRPl5QHRpaGzB2KFb3NFcc4Qby4vFVyvHKS4eX3KSEx-QxWBVBzBTy2fiKHmgdTKb_Ybi3huhBB97lYuFJegfeAANp7aXvI2QGMuRKHPF8MH36RElcMZnYx'

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()

    location = data['location']
    
    headers = {'Authorization': f'Bearer {YELP_API_KEY}'}
    params = {'term': 'doctors',
              'location': location,
              'limit': 50,
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

if __name__ == '__main__':
    app.run(debug=True)