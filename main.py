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

        message_text = f"🏙 {city}:\n🌡Температура: {weather_data['temp']}°C\nОщущается как: {weather_data['feels_like']}°C\n\nСостояние: {weather_data['description'].capitalize()}\n💨 Ветер: {weather_data['wind_speed']} м/с ({weather_data['wind_deg']}°)"

        bot.send_message(message.chat.id, message_text, reply_markup = keyboards.create_advice_keyboard(weather_data['temp'], weather_data['description']))
    else:
        bot.send_message(message.chat.id, f"Упс, похоже такого города нет в списке!")

# Обработка нажатия на кнопку "Рекомендации по одежде"
@bot.callback_query_handler(func=lambda call: True)
def callback_weather_advice(call):
    weather_data = call.data.split('_')

    temp = float(weather_data[1])
    description = weather_data[2]

    advice = weather.get_recomendation(temp, description)

    bot.answer_callback_query(call.id, advice)
    bot.edit_message_text(text=f'💡 Совет:\n{advice}', chat_id=call.message.chat.id, message_id=call.message.message_id)

if __name__ == "__main__":
    print("Бот запущен!")
    bot.polling(none_stop=True)