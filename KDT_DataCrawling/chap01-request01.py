from urllib.request import urlopen
from bs4 import BeautifulSoup

melon_url = 'http://www.melon.com/chart/index.htm'
html = urlopen(melon_url)

# HTTP Error 406: Not Aceeptable 발생
soup = BeautifulSoup(html.read(), 'html.parser')
print(soup)
