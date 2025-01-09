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
    feels_like = data['main']['feels_like']
    wind_speed = data['wind']['speed']
    wind_deg = data['wind']['deg']
    weather_description = data['weather'][0]['description']

    weather_data = {
        "temp": temp,
        "feels_like": feels_like,
        "wind_speed": wind_speed,
        "wind_deg": wind_deg,
        "description": weather_description
    }

    return weather_data

def get_recomendation(temp, description):
    if temp < -10:
        advice = "Морозно! Одевай очень теплую зимнюю куртку и валенки."
    elif -10 <= temp < 0:
        advice = 'Очень холодно! Наденьте теплую зимнюю одежду.'
    elif 0 <= temp < 10:
        advice = 'Холодно. Одевайтесь в теплую куртку и шарф.'
    elif 10 <= temp < 20:
        advice = 'Прохладно. Легкая куртка или свитер будет в самый раз.'
    elif 20 <= temp < 30:
        advice = 'Тепло. Легкая одежда, можно носить футболки.'
    elif temo >= 30:
        advice = 'Жарко. Обязательно носите летнюю одежду, шорты и футболки.'

    if 'дожд' in description.lower():
        advice += f"\n\nТакже не забудьте взять с собой зонтик или дождевик"

    return advice
