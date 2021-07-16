import requests
# https://api.telegram.org/bot{토큰}/setWebhook?url={pythonanywhere}

TOKEN = '1848729518:AAFAzKaAe_lr4CM0z67TVvJ7UqmjJ1WRudg'
pythonanywhere = 'SoominKim.pythonanywhere.com'
url = f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={pythonanywhere}/telegram'
print(requests.get(url))