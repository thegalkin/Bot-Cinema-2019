import telebot
bot = telebot.TeleBot('%773838642:AAFvElKnWJZMjyOiegGxLPDLneASy4Hpmaw%')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет" or message.text == "Начали" or message.text == "Покажи кинотеатры" or message.text == "Здравствуйте" or message.text == "Привет бот":
        bot.send_message(message.from_user.id,"Привет, выбери сеть кинотеатров: 1)Каро 2)... 3)...")
    else:
        bot.send_message(message.from_user.id, "Прости, я тебя не понимаю. Напиши мне Привет")

    bot.polling(none_stop=True, interval=0)