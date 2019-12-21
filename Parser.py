from bs4 import BeautifulSoup as BF
import requests as req

urls = "https://karofilm.ru/theatres"
todayKARO = open("Today_Parser_KARO_raw.txt", 'w')
contentsKARO = req.get(urls)
contentsKARO = BF(contentsKARO.text, "html.parser")
todayKARO.write(str(contentsKARO))