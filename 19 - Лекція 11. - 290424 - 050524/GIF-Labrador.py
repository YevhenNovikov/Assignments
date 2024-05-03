# A6N6ATguhkSqV6ohQmVr3Ip6x3GwkAxT


import requests

API_KEY = 'A6N6ATguhkSqV6ohQmVr3Ip6x3GwkAxT'
SEARCH_TERM = input() # Labrador

base_url = 'https://api.giphy.com/v1/'
endpoint = 'gifs/search'
PARAMS = {
    'api_key': API_KEY,
    'q': SEARCH_TERM,
    'limit': 5
}

URL = f"{base_url}{endpoint}"


resp = requests.get(URL, params=PARAMS)
print(resp.json())


data = resp.json()

for gif in data['data']:
    print(gif['url'])
    