import requests
def current_location():
    url = 'http://ipinfo.io/json'
    response = requests.get(url)
    data = response.json()
    city = data['city']
    return city