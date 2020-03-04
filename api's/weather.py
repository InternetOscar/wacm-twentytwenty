from urllib.request import urlopen
from secrets import *
import json

print(key)

# link that we are calling for our API program
link = 'https://api.openweathermap.org/data/2.5/weather?q=Joondalup,au&appid='

# open the link
wget = urlopen(link + key)

# read the info (to ram?)
webtext = wget.read()

# decode text and output
print(webtext.decode('utf-8'))
