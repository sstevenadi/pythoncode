from urllib.request import urlopen
import xml.etree.ElementTree as ET

data = urlopen('http://py4e-data.dr-chuck.net/comments_1199223.xml').read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum = 0

print ('Total data :',len(counts))
for items in counts:
    sum = sum + int(items.text)

print (sum)