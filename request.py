import requests
import time

url = 'https://server-6-.glitch.me/list'
data = {'username': 'admin', 'password': 'root'}

while True:
    response = requests.post(url, data=data)
    print(response.text)  # Print the response from the server
    time.sleep(240)  # Wait for 4 minutes
