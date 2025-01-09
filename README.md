<h1 align="center">Weather Telegram Bot</h1>
<h3 align="center">Бот для просмотра погоды в 5 городах и получения рекомендаций по одежде!</h3>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=О+проекте)](https://git.io/typing-svg)
Проект написан на языке программирования: ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

С использованием таких библиотек как:
1. Telebot - Для подключения к api Telegram
2. Requests - Для подключения к api OpemWeather (для получения данных о погоде)

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Функционал+проекта)](https://git.io/typing-svg)

Бот умеет определять погоду в 5 локациях РФ:
1. Москва
2. Санкт-Петербург
3. Владивосток
4. Казань
5. Краснодар

Также исходят из погоды, бот рекомендует какую одежды лучше одеть

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Запуск+проекта)](https://git.io/typing-svg)

Для запуска проекта необходимо:
1. Скачать библиотеки
```bash
pip install pyTelegramBotAPI requests
```

2. Клонировать проект
```bash
https://github.com/pofateeva/wether-telegram-bot.git
```

3. В корне проекта создать файл config.py
Внутри него прописать две переменных: с ключом для вашего Телеграм бота и api от [OpenWeather](https://home.openweathermap.org/api_keys)
```python
TELEGRAM_API_TOKEN = 'your-telegram-bot-token'
OPENWEATHER_API_TOKEN = 'your-api-key-from-openweather'
```

4. Далее в консоли запустите проект с помощью команды
```bash
python main.py
```

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Проект+был+сделан)](https://git.io/typing-svg)
Климовцовой Олесей и Фатеевой Полиной