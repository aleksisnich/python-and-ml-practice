import requests
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
from hdfs import InsecureClient

# # Конфигурация
# api_key = "29f874be26acac87e7e13e80f7a52d7b"  # Замените на ваш API ключ от OpenWeatherMap
# # Список городов
# cities = {
#     "London": {"lat": 51.5074, "lon": -0.1278},
#     "New York": {"lat": 40.7128, "lon": -74.0060},
#     "Tokyo": {"lat": 35.6895, "lon": 139.6917},
#     "Moscow": {"lat": 55.7558, "lon": 37.6176},
#     "Sydney": {"lat": -33.8688, "lon": 151.2093}
# }
#
# # Параметры запроса
# url = "https://api.openweathermap.org/data/3.0/onecall"
# data = []
#
# # Получение данных за последний месяц
# for city, coords in cities.items():
#     for i in range(30):
#         date = datetime.now() - timedelta(days=i)
#         timestamp = int(date.timestamp())
#         params = {
#             "lat": coords["lat"],
#             "lon": coords["lon"],
#             "dt": timestamp,
#             "appid": api_key,
#             "units": "metric"
#         }
#         response = requests.get(url, params=params)
#         if response.status_code == 200:
#             weather_data = response.json()
#             data.append({
#                 "city": city,
#                 "date": date.strftime("%Y-%m-%d"),
#                 "temp": weather_data["current"]["temp"]
#             })
#
# # Создание DataFrame
# df = pd.DataFrame(data)
#

# url = "https://api.openweathermap.org/data/3.0/onecall/timemachine"
# params = {
#             "lat": 39.099724,
#             "lon": -94.578331,
#             "dt": 1643803200,
#             "appid": "29f874be26acac87e7e13e80f7a52d7b"
# }
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
#            "Accept": "*/*"}
# response = requests.get(url, params=params, headers=headers)
# if response.status_code == 200:
#     print("Успешный запрос API")
# else:
#     print("Запрос API отклонен с кодом состояния: ", response.status_code)
#
#
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 51.5074,  # Широта
    "longitude": -0.1278,  # Долгота
    "hourly": "temperature_2m",  # Температура на высоте 2 метра
    "timezone": "auto"
}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
           "Accept": "*/*"}
response = requests.get(url, params=params, headers=headers)
print(response.json())
# print(df)
# plt.figure(figsize=(10, 6))
# for city in cities.items():
#     city_data = df[df["city"] == city]
#     plt.plot(city_data["date"], city_data["temp"], label=city)
#
# plt.xlabel("Date")
# plt.ylabel("Temperature (°C)")
# plt.title("Temperature Change Over Last Month")
# plt.legend()
# plt.show()