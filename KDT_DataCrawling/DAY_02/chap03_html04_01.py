from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

table_tag = soup.find('table', {'id':'giftList'})
# print('children 개수: ', len(list(table_tag.children)))
# for child in table_tag.children:
#     print(child)
#     print('-' * 30)

desc = soup.find('table', {'id':'giftList'}).descendants
list_desc = list(desc)
# print('descendants 개수: ', len(list_desc))
#
# for tag in list_desc:
#     print(tag)

# for sibling in table_tag.tr.next_siblings:
#     print(sibling)

# for sibling in soup.find('tr', {'id':'gift2'}).previous_siblings:
#     print(sibling)

sibling1 = soup.find('tr', {'id':'gift3'}).next_sibling
# print('sibiling1:', sibling1)
# print(ord(sibling1))

sibling2 = soup.find('tr', {'id':'gift3'}).next_sibling.next_sibling
# print(sibling2)

img1 = soup.find('img', {'src':'../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)