### 컴퓨터언어

- 어셈블리어: 저수준의 언어
> 명령을 내릴 때 디테일하게 내려야 됨
- C언어: 처음 등장했을 떄 센세이션
> 어셈블리어를 더 이해하기 쉽게
> 명령어 감소
- 파이썬: 더 사람이 쓰기 편하게
> 쉽다
> 많은 사람들이 사용
> 오픈 소스가 많아서 많은 것을 할 수 있다

### 프로그래밍 언어 3형식
> 저장
> 조건(if)
> 반복(while,for)

### 파이썬
> 저장 
- 변수: 메모리에 값을 저장하는 것
- 무엇을 저장? 숫자, 글자, 참/거짓
- 리스트: 여러 변수를 한번에 저장
'''python
> dust = [58, 40 70]
- 딕셔너리: key, value 값 매칭하여 저장
'''python
> dust = {'영등포구: 40, '강남구': 50}
- 함수
> 내장함수
> 사용자 정의 함수

- 모듈 랜덤
> import
> 함수 사용 
--random.choice(리스트) ->1개 뽑기
--random.sample(리스트, 뽑을 숫자) ->여러개 뽑기

- 조건문
> if 조건식:
> elif 조건식:
> else:

- 사칙연산
> 정수 / 정수해도 결과가 실수형이면 자동 형변환
>> Ex) 10/3 = 3.3333333
> 정수 // 정수 => 정수부분만 취함
> 10**3 = 10의 3승

- 문자열
> 비교연산: 사전순에 대한 판단
> 곱하기: 곱한만큼 반복

- 반복문
> while 조건식:
>> 조건식 true일때까지 반복
> for i in List:
>> 리스트 돌면서 반복
> for i in range (0,n):
>> 0부터 n-1만큼 반복

### import requests
- requests.get(주소)
- requests.get(주소).text
- requests.get(주소).status_code : 상태 반환. 200이면 정상적으로 응답한 것

### from bs4 import BeautifulSoup
- Response한 걸 처리하는 클래스
- BeautifulSoup(문서)
- BeautifulSoup(경로): 경로 안에 selector 들어가면 문서 안에 있는 특정 내용을 뽑아줘
- BeautifulSoup.select_one(경로)

'''python
url = 'https://~'
response = requests.get(url)
data = BeautifulSoup(response.text,lxml)
print(data.select_one('가져올 데이터의 selector).text)

### JSON(JavaScript Object Notation)
- 데이터만을 주고 받기 위한 표기법

### API(Application Programming Interface)
- OS와 응용프로그램 사이 데이터 주고 받기 위해 약속한 것, 규격을 정해놓은 것
- 실시간 업데이트 되는 정보를 활용하기 위해서는 API 필요
- 서비스와 서비스 간의 프로그래밍을 통한 대화방식
- 요청 받는 측에서 일정한 방식을 명세
- ex) 카카오톡 API, 페이스북 로그인, 공공데이터 API, 네이버지도 API, 코인 거래소
- 가이드를 활용하여 요청된 url을 넘김

