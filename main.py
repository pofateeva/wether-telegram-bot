import telebot
import keyboards
import weather
from config import TELEGRAM_API_TOKEN

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Выбери город, погоду которого ты хочешь узнать...", reply_markup = keyboards.city_keyboard)

@bot.message_handler(func=lambda message: message.text)
def get_city_weather(message):
    if message.text in keyboards.CITIES:
        city = message.text.strip()
        weather_data = weather.get_weather(city)

        if weather_data is None:
            bot.send_message(message.chat.id, "Не удалось получить погоду из города. Попробуй еще раз!")
            return

        temp, description = weather_data
        message_text = f"Погода в {city}:\nТемпература: {temp}°C\nСостояние: {description.capitalize()}"
        bot.send_message(message.chat.id, message_text)
    else:
        bot.send_message(message.chat.id, f"Упс, похоже такого города нет в списке!")

if __name__ == "__main__":
    print("Бот запущен!")
    bot.polling(none_stop=False)