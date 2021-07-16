from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'

token = '1848729518:AAFAzKaAe_lr4CM0z67TVvJ7UqmjJ1WRudg'
url = f'https://api.telegram.org/bot{token}/'


@app.route('/telegram', methods=['POST'])
def receive_telegram():
    # 텔레그램으로부터 수신한 요청(request)    
    response = request.get_json()
    
    if response.get('message') != None:
        chat_id = response.get('message').get('from').get('id')
        text = response.get('message').get('text')

        if text == '광주2반':
            answer = '광주2반 화이팅!!\n ㅎㅎㅎㅎㅎㅎㅎ'
        else:
            answer = '머선 소리고?'

        requests.get(url + f'sendMessage?chat_id={chat_id}&text={answer}')

    return '', 200