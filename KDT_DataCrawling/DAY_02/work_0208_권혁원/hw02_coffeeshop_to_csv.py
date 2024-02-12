from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

urlfront = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo='
urlback = '&sido=&gugun=&store='
frame = {'위치(시,구)':[], '매장이름':[], '주소':[], '전화번호':[]}

cnt = 1
for pageNo in range(1, 52):
    html = urlopen(urlfront+str(pageNo)+urlback)
    soup = BeautifulSoup(html, 'html.parser')

    fieldset = soup.select_one('fieldset > fieldset')
    trs = fieldset.select('tbody > tr')

    for row in trs:
        tds = row.select('td')
        frame['위치(시,구)'].append(tds[0].text)
        frame['매장이름'].append(tds[1].text)
        frame['주소'].append(tds[3].text)
        frame['전화번호'].append(tds[-1].text)
        print(f'[{cnt:>3}]: 매장이름: {tds[0].text}, 지역: {tds[1].text}, 주소: {tds[3].text}')
        cnt += 1

csv_name = 'hollys_branches.csv'
df = pd.DataFrame(frame)
df.to_csv(csv_name, encoding='utf-8')
print('전체 매장 수:', cnt-1)
print(csv_name, '파일 저장 완료')
