import requests
import time
import os

BOT_TOKEN = os.environ.get('6198152820:AAHRQ00aN5L2ZhrQ_W7Zz3xIdglbIT2lLnM')
CHAT_ID = os.environ.get('https://t.me/MarytheMar')
USERNAME = 'admin'
PASSWORD = 'root'
URL = 'https://server-6-.glitch.me/list'

def send_request():
    try:
        response = requests.get(URL, auth=(USERNAME, PASSWORD))
        message = f'Response status code: {response.status_code}'
        send_telegram_message(message)
    except Exception as e:
        message = f'An error occurred while sending the request: {str(e)}'
        send_telegram_message(message)

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print(f'An error occurred while sending the Telegram message: {response.text}')

while True:
    send_request()
    time.sleep(240) # sleep for 4 minutes

