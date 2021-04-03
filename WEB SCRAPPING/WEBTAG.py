from urllib.request import urlopen
from bs4 import BeautifulSoup

parser = "html.parser"
a = "http://py4e-data.dr-chuck.net/known_by_Kerrie.html"

for times in range(7):
    html = urlopen(a).read()
    soup = BeautifulSoup(html, parser)
    tags = soup('a')
    a = tags[17].get('href', None)
    print(a)
    