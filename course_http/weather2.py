import requests
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
from hdfs import InsecureClient

# Конфигурация
cities = {
    "London": {"lat": 51.5074, "lon": -0.1278},
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "Tokyo": {"lat": 35.6895, "lon": 139.6917},
    "Moscow": {"lat": 55.7558, "lon": 37.6176},
    "Sydney": {"lat": -33.8688, "lon": 151.2093}
}
hdfs_url = "http://namenode:50070"  # Замените на адрес вашего HDFS NameNode
hdfs_user = "nichi"  # Замените на вашего пользователя HDFS

# Сбор данных о погоде с Open-Meteo
def fetch_weather_data():
    url = "https://archive-api.open-meteo.com/v1/archive"
    data = []

    for city, coords in cities.items():
        # Определяем даты (последние 30 дней)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        params = {
            "latitude": coords["lat"],
            "longitude": coords["lon"],
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "hourly": "temperature_2m",
            "timezone": "auto"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            weather_data = response.json()
            for time, temp in zip(weather_data["hourly"]["time"], weather_data["hourly"]["temperature_2m"]):
                data.append({
                    "city": city,
                    "date": time,
                    "temp": temp
                })
        else:
            print(f"Ошибка запроса для {city}: {response.status_code}")

    return pd.DataFrame(data)

# Визуализация данных
def plot_weather_data(df):
    if df.empty:
        print("Нет данных для визуализации!")
        return

    # График изменения температуры
    plt.figure(figsize=(12, 6))
    for city in cities:
        city_data = df[df["city"] == city]
        if not city_data.empty:
            plt.plot(city_data["date"], city_data["temp"], label=city)
    plt.xlabel("Дата")
    plt.ylabel("Температура (°C)")
    plt.title("Изменение температуры за последний месяц")
    plt.legend()
    plt.xticks(rotation=45)  # Поворот меток дат для удобства
    plt.show()

    # График распределения температуры
    plt.figure(figsize=(10, 6))
    sns.histplot(df, x="temp", hue="city", multiple="stack", kde=True)
    plt.xlabel("Температура (°C)")
    plt.title("Распределение температуры")
    plt.show()

# Сохранение данных в HDFS
def save_to_hdfs(df, hdfs_path):
    if df.empty:
        print("Нет данных для сохранения в HDFS!")
        return

    client = InsecureClient(hdfs_url, user=hdfs_user)
    with client.write(hdfs_path, encoding="utf-8") as writer:
        df.to_csv(writer, index=False)
    print(f"Данные сохранены в HDFS: {hdfs_path}")

# Выгрузка данных из HDFS на локальный компьютер
def load_from_hdfs(hdfs_path, local_path):
    client = InsecureClient(hdfs_url, user=hdfs_user)
    with client.read(hdfs_path, encoding="utf-8") as reader:
        df = pd.read_csv(reader)
    df.to_csv(local_path, index=False)
    print(f"Данные выгружены из HDFS в: {local_path}")

# Основной код
if __name__ == "__main__":
    # 1. Сбор данных
    print("Сбор данных о погоде...")
    weather_df = fetch_weather_data()
    print("Данные собраны:")
    print(weather_df.head())  # Вывод первых строк данных для проверки

    # 2. Визуализация
    print("Визуализация данных...")
    plot_weather_data(weather_df)

    # 3. Сохранение в HDFS
    hdfs_path = "/user/hadoop_user/weather_data.csv"
    print(f"Сохранение данных в HDFS: {hdfs_path}")
    save_to_hdfs(weather_df, hdfs_path)

    # 4. Выгрузка из HDFS на локальный компьютер
    local_path = "weather_data_local.csv"
    print(f"Выгрузка данных из HDFS в: {local_path}")
    load_from_hdfs(hdfs_path, local_path)