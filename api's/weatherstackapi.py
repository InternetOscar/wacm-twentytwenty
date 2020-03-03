from urllib.request import URLopener

# link that we are calling for our API program
link = 'http://wttr.in/Perth?format=3'

# open the link
wget = urlopen(link)

# read the info (to ram?)
webtext = wget.read()

# decode text and output
print(webtext.decode('utf-8'))