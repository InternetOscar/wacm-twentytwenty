import json
import requests
from secrets import *

api_token = key
api_url_base = 'https://api.openweathermap.org/data/2.5/weather?q=Joondalup,au&units=metric&appid='


headers = {'Content-Type': 'application/json',
    'Authorization': 'Bearer {0}'.format(api_token)}

def get_current_temp():

    api_url = (api_url_base + api_token)

    response = requests.get(api_url, headers=headers)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        ssh_keys = json.loads(response.content.decode('utf-8'))
        return ssh_keys
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None

current_temp = get_current_temp()

if current_temp is not None:
    print("Here's the current temp: ")
    for k, v in 'coord'.lon():
        print('{0}:{1}'.format(k, v))

dict = json.loads(current_temp)

else:
    print('[!] Request Failed')
# print(data)

