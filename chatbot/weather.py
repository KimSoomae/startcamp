#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

url = 'https://www.metaweather.com/api/location/1132599/'
response = requests.get(url).json()
weather = response["consolidated_weather"][2]["weather_state_name"]
print(weather)
print(f'서울의 모레 날씨는 {weather}로 예상됩니다.')