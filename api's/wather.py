from urllib.request import urlopen
from secrets import *
import json

print(key)

# #read JSON file
# with open('keys.json', 'r') as myfile:
#     data=myfile.read()

# # parse zee file
# obj = json.loads(data)

# #load the values
# print("key: " + str(obj['key']))

# # link that we are calling for our API program
# link = 'http://wttr.in/Perth?format=3'

# # open the link
# wget = urlopen(link)

# # read the info (to ram?)
# webtext = wget.read()

# # decode text and output
# print(webtext.decode('utf-8'))