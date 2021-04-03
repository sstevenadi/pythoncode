import urllib.error, urllib.parse, urllib.request
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Where it is : ')

url = serviceurl + urllib.parse.urlencode({'address' : address , 'key' : 42})
data = urllib.request.urlopen(url)
thething =  json.loads(data.read().decode())

print(f"Place Id : {thething['results'][0]['place_id']}")