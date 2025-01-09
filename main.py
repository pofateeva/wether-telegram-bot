import telebot
from config import TELEGRAM_API_TOKEN

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для вывода погоды!")

if __name__ == "__main__":
    print("Бот запущен!")
    bot.polling(none_stop=True)