import requests
from pprint import pprint

token = '1848729518:AAFAzKaAe_lr4CM0z67TVvJ7UqmjJ1WRudg' 
APP_URL = f'https://api.telegram.org/bot{token}'

key = 'iTpdD5hhMW71PQus57ztCitlpMM8T4ntl3mEe%2FTzhseoUcgTpG5kR29kq7%2FcxYy4ky3ufUl%2B5wvT5JURzmFmTg%3D%3D'
dust_url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=5&pageNo=1&sidoName=서울&ver=1.0&returnType=json'

dust_response = requests.get(dust_url).json()

update_url = f'{APP_URL}/getUpdates'
response = requests.get(update_url).json()

chat_id = response.get('result')[0].get('message').get('chat').get('id')
sido_name = dust_response["response"]["body"]["items"][0]["sidoName"]
dust = dust_response["response"]["body"]["items"][0]["pm10Value"]
dustmessage = f'오늘 {sido_name}의 미세먼지는 {dust}입니다.'
message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={dustmessage}'

print(requests.get(message_url))
