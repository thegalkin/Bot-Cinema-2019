import vk_api
import requests
import time
import random

"""vk_session = vk_api.VkApi(token='ad706b00ddc233907a509da6bbf3721ab996732b5a21c321c17ca6176dd363d2d3e9f9a13610cde63f5f5')
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:
        if event.text == 'Привет' or event.text == 'Покажи кинотеатры': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Привет, выбери сеть кинотеатров: 1)Каро 2)... 3)...'
		)
            elif event.from_chat: #Если написали в Беседе
                vk.messages.send( #Отправляем собщение
                    chat_id=event.chat_id,
                    message='Привет, выбери сеть кинотеатров: 1)Каро 2)... 3)...'
		)"""
vk = vk_api.VkApi(token='ad706b00ddc233907a509da6bbf3721ab996732b5a21c321c17ca6176dd363d2d3e9f9a13610cde63f5f5')

vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет, выбери сеть кинотеатров: 1)Каро 2)... 3)...", "random_id": random.randint(1, 2147483647)})

            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()), "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)










"""def get_text_messages(message):
    if message.text == "Привет" or message.text == "Начали" or message.text == "Покажи кинотеатры" or message.text == "Здравствуйте" or message.text == "Привет бот":
        bot.send_message(message.from_user.id,"Привет, выбери сеть кинотеатров: 1)Каро 2)... 3)...")
    else:
        bot.send_message(message.from_user.id, "Прости, я тебя не понимаю. Напиши мне Привет")

bot.polling(none_stop=True, interval=0)
"""