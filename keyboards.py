from telebot import types

# Создание клваиатуры для выбора городов
CITIES = ["Москва", "Санкт-Петербург", "Владивосток", "Казань", "Краснодар"]
city_keyboard = types.ReplyKeyboardMarkup(row_width=3)

city_buttons = [types.KeyboardButton(city) for city in CITIES]
city_keyboard.add(*city_buttons)

def create_advice_keyboard(temp, description):
    advice_keyboard = types.InlineKeyboardMarkup()
    advice_button = types.InlineKeyboardButton("🧣 Рекомендации по одежде", callback_data=f'rec_{temp}_{description}')
    advice_keyboard.add(advice_button)

    return advice_keyboard