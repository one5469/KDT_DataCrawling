import requests
from bs4 import BeautifulSoup

url1 = 'http://www.pythonscraping.com/pages/page1.html'
url2 = 'http://finance.naver.com'
url3 = 'http://www.naver.com'

html = requests.get(url1)
print('html.encoding:', html.encoding)
print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

print()
print('h1.string:', soup.h1.string)