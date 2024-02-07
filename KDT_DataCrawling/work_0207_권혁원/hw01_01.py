import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 길이 출력 함수
def printLength(list):
    print('총 tomestone-container 검색 개수: ', len(list))


# find 이용 함수
def scraping_use_find(html):
    soup = BeautifulSoup(html.read(), 'html.parser')

    main = soup.find('main')        # main 부분을 먼저 추출

    # 단계적으로 부분 줄이기
    divs = main.find('div', attrs={'class':'contentArea'})
    deepdiv = divs.find(attrs={'id':'seven-day-forecast',
                               'class':'panel panel-default'})
    ul = deepdiv.find('ul', attrs={'id':'seven-day-forecast-list',
                                   'class':'list-unstyled'})
    # tombstone-container 리스트 생성
    tombstoneList = ul.find_all('div', attrs={'class':'tombstone-container'})
    detailed = divs.find('div', attrs={'class':'panel-body',
                                       'id':'detailed-forecast-body'})
    # detailed 리스트 생성
    detailedList = detailed.find_all(attrs={'class':'row'})

    print('[find] 함수 사용')
    printLength(tombstoneList)

    for ts, dt in zip(tombstoneList, detailedList):
        print('--------------------------------------------------------------------------------')
        print(f'[Period]: {ts.find("p").text}')
        print(f'[Short desc]: {ts.find("p", attrs={"class":"short-desc"}).text}')
        try:
            print(f'[Temperature]: {ts.find("p", attrs={"class":"temp"}).text}')
        except AttributeError:
            print(f'[Temperature]: None')
        print(f'[Image desc]: {dt.find(attrs={"class":"col-sm-2"}).text}: '
              f'{dt.find(attrs={"class":"col-sm-10"}).text}')


# select 이용 함수
def scraping_use_select(html):
    soup = BeautifulSoup(html.read(), 'html.parser')

    main = soup.select_one('main')  # main 부분을 먼저 추출

    # 단계적으로 부분 줄이기
    divs = main.select_one('div.contentArea')
    deepdiv = divs.select_one('#seven-day-forecast')
    ul = deepdiv.select_one('ul#seven-day-forecast-list')
    # tombstone-container 리스트 생성
    tombstoneList = ul.select('div.tombstone-container')
    detailed = divs.select_one('div#detailed-forecast-body')
    # detailed 리스트 생성
    detailedList = detailed.select('.row')

    print('[select] 함수 사용')
    printLength(tombstoneList)

    for ts, dt in zip(tombstoneList, detailedList):
        print('--------------------------------------------------------------------------------')
        print(f'[Period]: {ts.select_one("p").text}')
        print(f'[Short desc]: {ts.select_one("p.short-desc").text}')
        try:
            print(f'[Temperature]: {ts.select_one("p.temp").text}')
        except AttributeError:
            print(f'[Temperature]: None')
        print(f'[Image desc]: {dt.select_one(".col-sm-2").text}: '
              f'{dt.select_one(".col-sm-10").text}')

# 링크
url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY'

# html 정보
html = urlopen(url)
html2 = urlopen(url)

print('National Weather Service Scraping')
print('----------------------------------')
scraping_use_find(html)
print('--------------------------------------------------------------------------------')
scraping_use_select(html2)