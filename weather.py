import requests
from config import OPENWEATHER_API_TOKEN

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_TOKEN}&units=metric&lang=ru'
    response = requests.get(url)
    data = response.json()

    # Проверка на успешный запрос
    if data.get('cod') != 200:
        print("Ошибка получения данных о погоде.")
        return None

    # Извлечение данных о температуре и погодных условиях
    temp = data['main']['temp']
    weather_description = data['weather'][0]['description']
    return temp, weather_description