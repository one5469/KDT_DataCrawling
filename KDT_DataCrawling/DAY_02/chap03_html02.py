from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

nameList = soup.find_all('span', {'class':'green'})
for name in nameList:
    print(name.string)

princeList = soup.find_all(string='the prince')
print(princeList)
print('the prince count: ', len(princeList))