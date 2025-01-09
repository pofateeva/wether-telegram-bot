import telebot
import keyboards
from config import TELEGRAM_API_TOKEN

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Выбери город, погоду которого ты хочешь узнать...", reply_markup = keyboards.city_keyboard)

@bot.message_handler(func=lambda message: message.text)
def get_city_weather(message):
    if message.text in keyboards.CITIES:
        city = message.text.strip()
        bot.send_message(message.chat.id, f"Вы выбрали город: {city}")
    else:
        bot.send_message(message.chat.id, f"Упс, похоже такого города нет в списке!")

if __name__ == "__main__":
    print("Бот запущен!")
    bot.polling(none_stop=False)