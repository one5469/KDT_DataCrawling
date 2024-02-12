from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

melon_url = 'http://www.melon.com/chart/index.htm'
urlrequest = Request(melon_url, headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(urlrequest)
soup = BeautifulSoup(html.read(), 'html.parser')

print(soup)
