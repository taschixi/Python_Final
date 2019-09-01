import urllib.request
import json
import webbrowser

# Define APOD
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=QVrAV1iInFPMWnn3tTRdF6vi5WuSMnR1dfHK4h7I'

# Call the webservice
apodurlobj = urllib.request.urlopen(apodurl + mykey)

# read the file-like object
apodurlread = apodurlobj.read()

# decode the json to python
decodeapod = json.loads(apodurlread.decode('utf-8'))

# Display the data
print("\n\nConverted python data")
print(decodeapod)

# Use your browser to open the URL
# input('\nPress Enter to open NASA Picture of the Day in your web browser')
webbrowser.open(decodeapod['url'])