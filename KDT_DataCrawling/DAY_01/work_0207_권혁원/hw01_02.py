from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote

# 시간대별 날씨 및 온도 출력 함수
def printDaytime(hourly):
    print('-----------------------')
    print('시간대별 날씨 및 온도')
    print('-----------------------')

    # 시간대별 정보 리스트
    hours = hourly.select('li')

    for h in hours:
        print(f'{h.select_one("dt.time").text}  '
              f'{h.select_one("span.blind").text}\t'
              f'{h.select_one("span.num").text}'
              )

# 오늘 날씨 정보 출력 함수
def printWeatherInfo(loc, weather):
    print('현재 위치: ', loc.select_one('h2.title').text)
    print('현재 온도: ', weather.select_one('div.temperature_text').text)
    print('날씨 상태: ', weather.select_one('div.weather_main').text)
    chart_list = weather.select_one('ul.today_chart_list')
    print('공기 상태: ')
    for chart in chart_list.select('li'):
        print(chart.text.strip())


def main():
    url = f'https://search.naver.com/search.naver?query={quote("대구 + 날씨")}'

    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')

    # html의 메인 파트 가져오기
    main = soup.find('div', attrs={'id':'container',
                                   'role':'main'})
    # 자르기
    part = main.select_one('div.open')

    # 위치 정보
    loc = main.select_one('div.title_area')
    # 오늘 날씨 정보
    weather = part.select_one('div.weather_info')
    # 시간대별 정보
    hourly = part.select_one('div._hourly_weather')

    printWeatherInfo(loc, weather)
    printDaytime(hourly)

main()