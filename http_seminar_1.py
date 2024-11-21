import requests
import json
from pprint import pprint
# import os
# from dotenv import load_dotenv
# dotenv_path = os.path.join(os.path.dirname('.env'))
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)

url = "https://api.giphy.com/v1/gifs/search"
api_key = "y1fFYUEyHPNV0k69lvRGY4piZM0vbcSF" #os.getenv("api_key")
params = {"api_key": api_key,
          "q": "science",
          "limit": 5,
          "offset": 0,
          "rating": "pg-13",
          "lang": "ru",
          "bundle": "messaging_non_clips"}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
           "Accept": "*/*"}

response = requests.get(url, params=params, headers=headers)

# response.headers
# response.status_code
# response.ok
# response.text
# response.content - в бинарном виде

if response.status_code == 200:
    print("Успешный запрос API")
else:
    print("Запрос API отклонен с кодом состояния: ", response.status_code)

data = response.json()
with open('gifs.json', 'w') as f:
    json.dump(data, f)

for gif in data.get('data'):
    print(gif.get('images').get('original').get('url'))
pprint(data)


