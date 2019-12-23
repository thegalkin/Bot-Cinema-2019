import vk_api
import requests
import time
import random


vk = vk_api.VkApi(token='ad706b00ddc233907a509da6bbf3721ab996732b5a21c321c17ca6176dd363d2d3e9f9a13610cde63f5f5')

vk._auth_token()
cinemasDicti = open("Today_Parser_KARO_cinemas.txt", 'r')
filmsDicti = open("Today_Parser_KARO_films.txt", 'r')

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет, выбери кинотеатр из списка", "random_id": random.randint(1, 2147483647)})
                for i, j in enumerate(cinemasDicti.key()):
                    vk.method("messages.send", {"peer_id": id, "message": cinemasDicti[] + ") " + str(i),
                                                "random_id": random.randint(1, 2147483647)})
                listOfChoices = [j for j in range(len(cinemasDicti))]
            if body.lower() in listOfChoices:
                for i in enumerate(filmsDicti):
                    vk.method("messages.send", {"peer_id": id,"message": str(), "random_id": random.randint(1, 2147483647)})
                    #vk.method("messages.send", {"peer_id": id, "message": str(j) + ")" + "Выбери фильм из доступных сегодня:" + str(filmsDicti[i].keys()), "random_id": random.randint(1, 2147483647)})

        #    elif body.lower() != "привет:
              #  vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()), "random_id": random.randint(1, 2147483647)})

    except Exception as E:
        time.sleep(1)
