from bs4 import BeautifulSoup as BF
import re
import requests as req
import sqlite3

todayKARO_raw = open("Today_Parser_KARO_raw.txt", 'r')
todayKARO = open("Today_Parser_KARO.txt", 'w')

soup = BF(todayKARO_raw, "html.parser")
theatres = soup.findAll('li', {'class' : 'cinemalist__cinema-item'})


def remove_all(string):
    pattern = re.compile(r'[А-Яа-яёЁ0-9 ]+')
    return pattern.findall(string)[0].strip()
def removerForFormat(string):
    pattern = re.compile(r"[\S]")
    return ''.join(pattern.findall(string))
def findAllTheatres(theatres):
    global dataIds
    dataIds = []

    theatresDicti = {}
    for theater in theatres:
        dataIds.append(theater['data-id'])
        theatresDicti[theater.findAll('h4')[0].text] = {
            'metro': [remove_all(i.text) for i in theater.findAll('li', {"class" : "cinemalist__cinema-item__metro__station-list__station-item"})],
            'address': theater.findAll('p')[0].text.split('+')[0].strip(),
            'phone': '+' + theater.findAll('p')[0].text.split('+')[-1],
            'data-id': theater['data-id']
        }
    return theatresDicti
theatresDicti = findAllTheatres(theatres)

def inCinema(key):
    filmsDicti = {}
    cinemaUrl = "https://karofilm.ru/theatres?id=" + str(key)
    soup = BF(req.get(cinemaUrl).text, "html.parser")
    films = soup.findAll('div', class_='cinema-page-item__schedule__row__data')
    for film in films:
        filmsDicti[film.findAll('h3')[0].text] = {
            removerForFormat(film.findAll("div", class_= "cinema-page-item__schedule__row__board-row__left")[0].text) :
             [i. text for i in film.findAll('div', class_ = 'cinema-page-item__schedule__row__board-row__right')[0].findAll('a')]
        }

    return(filmsDicti)

filmsDicti = {}
print(dataIds)
filmsByIds = {key: inCinema(key) for key in dataIds}
print(filmsByIds)

con = sqlite3.connect('cinemasKaro.db')
cur = con.cursor()
print(theatresDicti)
cur.execute("""CREATE TABLE IF NOT EXISTS cinemas_karo( 
                     cinema_id INTEGER,
                     cinema_name TEXT,
                     cinema_address TEXT,
                     cinema_metro TEXT, 
                     cinema_phone TEXT)""")
con.commit()
theatresFordb = [theatresDicti.["data-id"].values(), theatresDicti.keys(), theatresDicti["address"].values(), theatresDicti["metro"].values(), theatresDicti["phone"].values()]
cur.executemany(f"insert or replace into cinemas_karo values(?,?,?,?,?)", theatresFordb)
con.commit()
cur.execute("""CREATE TABLE films_karo(
                    cinema_id INTEGER,  
                    film TEXT,
                    format TEXT,
                    times TEXT)

""")
con.commit()
id = None
film = None
format = None
for id, film in filmsByIds.items():
    print(id, film)
    cur.execute(f'insert or replace into films_karo(cinema_id) values ("{id}")')
    cur.execute(f'insert or replace into films_karo(film) values ("{film}")')
    for format, times in film:
        print(format, times)
        cur.execute(f'insert or replace into films_karo(format, times) values ("{format}", "{times}")')
con.commit()
cur.close()
con.close()
"""for c, d in enumerate(karo_theaters_films[film]):
        for e, f in enumerate(karo_theaters_films[b][d]):
            print(d)"""






