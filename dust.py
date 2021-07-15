import requests
from bs4 import BeautifulSoup


KEY = 'iTpdD5hhMW71PQus57ztCitlpMM8T4ntl3mEe%2FTzhseoUcgTpG5kR29kq7%2FcxYy4ky3ufUl%2B5wvT5JURzmFmTg%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.0'
# print(url)
response = requests.get(url)
data = BeautifulSoup(response.text, 'lxml')
# print(data)
item = data('item')[7]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')


# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.
if dust>150:
    print('미세먼지 매우나쁨')
elif dust>80:
    print('미세먼지 나쁨')
elif dust>30:
    print('미세먼지 보통')
else:
    print('미세번지 좋음')