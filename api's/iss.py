import requests
import json

response = requests.get("http://api.open-notify.org/iss-pass.json")

print(response.json())


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

pass_times = response.json()['response']
jprint(pass_times)