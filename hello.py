import requests
from bs4 import BeautifulSoup


url = 'https://finance.naver.com/sise/'
response = requests.get(url)

data = BeautifulSoup(response.text,"lxml")


print(data.select_one('#KOSPI_now'))
print(data.select_one('#KOSPI_now').text)

url='https://finance.naver.com/marketindex/'
response = requests.get(url)

data = BeautifulSoup(response.text,"lxml")

print(data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text)
