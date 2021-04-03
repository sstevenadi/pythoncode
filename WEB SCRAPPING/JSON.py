from urllib.request import urlopen
import json

data = urlopen('http://py4e-data.dr-chuck.net/comments_1199224.json').read()
count = json.loads(data)
sum = 0

for items in count['comments']:
    sum += int(items['count'])

print(sum)
