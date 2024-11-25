# Сценарий Foursquare
# Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию
# (например, кофейни, музеи, парки и т.д.).
# Используйте API Foursquare для поиска заведений в указанной категории.

import requests
import json
from pprint import pprint
from API_key import key

api_key = key

url = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
quer = input("Введите интересующее вас заведение или локации: ")
city = input("Введите город: ")
params = {"query": quer,
          "max_price": 4,
          "limit": 5,
          "near": city
}


headers = {
    "accept": "application/json",
    "Authorization": api_key
}

# Отправка запроса API и получение ответа
response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    print("Успешный запрос API")
    print("\n")
else:
    print("Запрос API отклонен с кодом состояния: ", response.status_code)

data = response.json()
with open('foursquare.json', 'w') as f:
    json.dump(data, f, indent=4)

for place in data.get('results'):
    print("Название заведения или локации: ", place.get('name'))
    print("Адрес заведения или локации: ", place.get('location').get('formatted_address'))
    print("Страна: ", place.get('location').get('country'))
    print("\n")
# pprint(data)

