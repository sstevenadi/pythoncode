from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://py4e-data.dr-chuck.net/comments_42.html').read()
x = BeautifulSoup(html, "html.parser")

tags = x('span')
sum = 0
for tag in tags:
    sum = sum + int(tag.contents[0])

print(sum)