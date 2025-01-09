from telebot import types

# Создание клваиатуры для выбора городов
CITIES = ["Москва", "Санкт-Петербург", "Владивосток", "Казань", "Краснодар"]
city_keyboard = types.ReplyKeyboardMarkup(row_width=3)

city_buttons = [types.KeyboardButton(city) for city in CITIES]
city_keyboard.add(*city_buttons)

